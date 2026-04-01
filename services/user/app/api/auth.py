"""用户认证 API 路由"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_REFRESH_TOKEN_EXPIRE_DAYS
from app.core.database import get_db
from app.core.redis_client import get_redis, RedisKeys
from app.models import User, AuthCredential
from app.schemas.auth import (
    UserRegisterRequest,
    UserLoginRequest,
    AuthResponse,
    TokenResponse,
    UserResponse,
    RefreshTokenRequest,
    MessageResponse,
)
from app.utils.jwt_handler import (
    create_access_token,
    create_refresh_token,
    verify_access_token,
    verify_refresh_token,
)
from app.utils.password_handler import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Authentication"])

# HTTP Bearer 认证方案
security = HTTPBearer(auto_error=False)


async def get_current_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
) -> Optional[str]:
    """从 Authorization header 提取 token"""
    if credentials:
        return credentials.credentials
    return None


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def register(
    request: UserRegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    """用户注册（含参数校验、密码 bcrypt 加密）"""
    # 检查用户名或邮箱是否已存在
    result = await db.execute(
        select(User).where(
            or_(User.username == request.username, User.email == request.email)
        )
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        if existing_user.username == request.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="用户名已被使用"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已被注册"
            )

    # 创建用户（密码 bcrypt 加密）
    password_hash = hash_password(request.password)
    user = User(
        username=request.username,
        email=request.email,
        password_hash=password_hash,
        nickname=request.nickname or request.username,
        age=request.age,
    )
    db.add(user)
    await db.flush()

    # 生成 Token（access 30min, refresh 7days）
    access_token = create_access_token(user.id, user.username, user.role)
    refresh_token = create_refresh_token(user.id)

    # 保存认证凭据
    credential = AuthCredential(
        user_id=user.id,
        access_token_hash=access_token[:50],  # 简化处理，实际应存储 hash
        refresh_token_hash=refresh_token[:50],
        token_expires_at=datetime.utcnow() + timedelta(days=JWT_REFRESH_TOKEN_EXPIRE_DAYS),
        last_login_at=datetime.utcnow(),
        login_count=1,
    )
    db.add(credential)
    await db.commit()

    return AuthResponse(
        user=UserResponse.model_validate(user),
        tokens=TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        ),
    )


@router.post("/login", response_model=AuthResponse)
async def login(
    request: UserLoginRequest,
    db: AsyncSession = Depends(get_db),
):
    """用户登录（返回 access_token + refresh_token）"""
    # 查找用户（支持用户名或邮箱登录）
    result = await db.execute(
        select(User).where(
            or_(User.username == request.username, User.email == request.username)
        )
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="账户已被禁用"
        )

    # 生成 Token（access 30min, refresh 7days）
    access_token = create_access_token(user.id, user.username, user.role)
    refresh_token = create_refresh_token(user.id)

    # 更新认证凭据
    cred_result = await db.execute(
        select(AuthCredential).where(AuthCredential.user_id == user.id)
    )
    credential = cred_result.scalar_one_or_none()

    if credential:
        credential.access_token_hash = access_token[:50]
        credential.refresh_token_hash = refresh_token[:50]
        credential.token_expires_at = datetime.utcnow() + timedelta(days=JWT_REFRESH_TOKEN_EXPIRE_DAYS)
        credential.last_login_at = datetime.utcnow()
        credential.login_count += 1
    else:
        credential = AuthCredential(
            user_id=user.id,
            access_token_hash=access_token[:50],
            refresh_token_hash=refresh_token[:50],
            token_expires_at=datetime.utcnow() + timedelta(days=JWT_REFRESH_TOKEN_EXPIRE_DAYS),
            last_login_at=datetime.utcnow(),
            login_count=1,
        )
        db.add(credential)

    await db.commit()

    return AuthResponse(
        user=UserResponse.model_validate(user),
        tokens=TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        ),
    )


@router.post("/logout", response_model=MessageResponse)
async def logout(
    token: Optional[str] = Depends(get_current_token),
    redis=Depends(get_redis),
):
    """用户登出（Token 黑名单）"""
    if token:
        # 验证并解析 token
        payload = verify_access_token(token)
        if payload:
            # 获取过期时间，计算 TTL
            exp = payload.get("exp", 0)
            ttl = max(0, exp - int(datetime.utcnow().timestamp()))
            # 将 token 加入黑名单
            await redis.setex(
                RedisKeys.token_blacklist(token[:50]),
                ttl,
                "1"
            )

    return MessageResponse(message="登出成功")


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    request: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
    redis=Depends(get_redis),
):
    """Token 刷新"""
    # 验证刷新令牌
    payload = verify_refresh_token(request.refresh_token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的刷新令牌"
        )

    user_id = payload.get("sub")

    # 检查是否在黑名单中
    is_blacklisted = await redis.get(RedisKeys.token_blacklist(request.refresh_token[:50]))
    if is_blacklisted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="令牌已失效"
        )

    # 查询用户
    result = await db.execute(select(User).where(User.id == UUID(user_id)))
    user = result.scalar_one_or_none()

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户不存在或已禁用"
        )

    # 生成新的访问令牌（access 30min）
    new_access_token = create_access_token(user.id, user.username, user.role)

    return TokenResponse(
        access_token=new_access_token,
        refresh_token=request.refresh_token,  # 保持原刷新令牌
        expires_in=JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
