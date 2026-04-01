"""认证相关 Pydantic Schemas"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserRegisterRequest(BaseModel):
    """用户注册请求"""
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=6, max_length=100, description="密码")
    nickname: Optional[str] = Field(None, max_length=100, description="昵称")
    age: Optional[int] = Field(None, ge=12, le=14, description="年龄 (12-14岁)")

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError("用户名只能包含字母和数字")
        return v


class UserLoginRequest(BaseModel):
    """用户登录请求"""
    username: str = Field(..., description="用户名或邮箱")
    password: str = Field(..., description="密码")


class TokenResponse(BaseModel):
    """Token 响应"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(BaseModel):
    """用户信息响应"""
    id: UUID
    username: str
    email: str
    nickname: Optional[str]
    avatar_url: Optional[str]
    age: Optional[int]
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    """认证响应（登录/注册）"""
    user: UserResponse
    tokens: TokenResponse


class RefreshTokenRequest(BaseModel):
    """刷新令牌请求"""
    refresh_token: str


class MessageResponse(BaseModel):
    """通用消息响应"""
    message: str