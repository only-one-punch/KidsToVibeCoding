"""限流中间件"""
import time
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Optional
import redis.asyncio as redis
import os


class RateLimitMiddleware(BaseHTTPMiddleware):
    """限流中间件 - 支持用户级、IP级、AI接口限流"""
    
    def __init__(self, app, redis_url: str = None):
        super().__init__(app)
        self.redis_url = redis_url or os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.redis: Optional[redis.Redis] = None
        
        # 限流配置
        self.user_limit = 100  # 用户每分钟请求数
        self.ip_limit = 60     # IP 每分钟请求数
        self.ai_limit = 20     # AI 接口每分钟请求数
    
    async def get_redis(self) -> redis.Redis:
        """获取 Redis 连接"""
        if self.redis is None:
            self.redis = redis.from_url(self.redis_url)
        return self.redis
    
    async def check_rate_limit(
        self,
        key: str,
        limit: int,
        window: int = 60
    ) -> tuple[bool, int]:
        """
        检查限流
        返回: (是否允许, 剩余配额)
        """
        client = await self.get_redis()
        current = int(time.time())
        window_start = current - (current % window)
        
        redis_key = f"ratelimit:{key}:{window_start}"
        
        try:
            count = await client.incr(redis_key)
            if count == 1:
                await client.expire(redis_key, window)
            
            remaining = max(0, limit - count)
            return count <= limit, remaining
        except Exception:
            # Redis 不可用时放行
            return True, limit
    
    async def dispatch(self, request: Request, call_next):
        """处理请求"""
        # 跳过健康检查
        if request.url.path in ["/health", "/ready", "/", "/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)
        
        # 获取用户 ID（如果已认证）
        user_id = request.headers.get("X-User-ID")
        client_ip = request.client.host if request.client else "unknown"
        
        # AI 接口限流
        if "/chat/" in request.url.path or "/voice/" in request.url.path:
            limit_key = f"ai:{user_id or client_ip}"
            allowed, remaining = await self.check_rate_limit(limit_key, self.ai_limit)
            if not allowed:
                raise HTTPException(
                    status_code=429,
                    detail="AI 接口请求过于频繁，请稍后再试"
                )
        
        # 用户级限流
        if user_id:
            allowed, remaining = await self.check_rate_limit(f"user:{user_id}", self.user_limit)
            if not allowed:
                raise HTTPException(
                    status_code=429,
                    detail="请求过于频繁，请稍后再试"
                )
        
        # IP 级限流
        allowed, remaining = await self.check_rate_limit(f"ip:{client_ip}", self.ip_limit)
        if not allowed:
            raise HTTPException(
                status_code=429,
                detail="请求过于频繁，请稍后再试"
            )
        
        response = await call_next(request)
        
        # 添加限流头
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        
        return response
