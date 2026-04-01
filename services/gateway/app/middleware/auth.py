"""认证中间件模块"""
import os
from datetime import datetime
from typing import Optional
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import BaseModel


# JWT 配置
JWT_SECRET = os.getenv("JWT_SECRET", "your-super-secret-jwt-key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# API Key 配置
SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "your-service-api-key")

security = HTTPBearer(auto_error=False)


class TokenPayload(BaseModel):
    """Token 载荷"""
    sub: str  # user_id
    exp: datetime
    iat: datetime
    type: str  # access / refresh


class UserInfo(BaseModel):
    """用户信息"""
    user_id: str
    is_authenticated: bool = False


async def verify_jwt_token(token: str) -> Optional[TokenPayload]:
    """验证 JWT Token"""
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )
        return TokenPayload(**payload)
    except JWTError:
        return None


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
) -> UserInfo:
    """获取当前用户（从 JWT Token）"""
    if credentials is None:
        return UserInfo(user_id="", is_authenticated=False)

    token = credentials.credentials
    payload = await verify_jwt_token(token)

    if payload is None:
        return UserInfo(user_id="", is_authenticated=False)

    return UserInfo(
        user_id=payload.sub,
        is_authenticated=True
    )


async def require_auth(
    user: UserInfo = Depends(get_current_user)
) -> UserInfo:
    """要求用户已认证"""
    if not user.is_authenticated:
        raise HTTPException(
            status_code=401,
            detail="未授权：无效或过期的 Token"
        )
    return user


def verify_api_key(api_key: str) -> bool:
    """验证服务间 API Key"""
    return api_key == SERVICE_API_KEY


async def require_api_key(request: Request) -> bool:
    """要求有效的 API Key（服务间调用）"""
    api_key = request.headers.get("X-API-Key")

    if not api_key or not verify_api_key(api_key):
        raise HTTPException(
            status_code=403,
            detail="无效的 API Key"
        )
    return True


class AuthMiddleware:
    """认证中间件"""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive)

            # 提取 Token 并验证
            auth_header = request.headers.get("Authorization", "")
            if auth_header.startswith("Bearer "):
                token = auth_header[7:]
                payload = await verify_jwt_token(token)
                if payload:
                    # 将用户信息注入到 scope 中
                    scope["user"] = {
                        "user_id": payload.sub,
                        "is_authenticated": True
                    }
                else:
                    scope["user"] = {"user_id": "", "is_authenticated": False}
            else:
                scope["user"] = {"user_id": "", "is_authenticated": False}

        await self.app(scope, receive, send)