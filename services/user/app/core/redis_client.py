"""Redis connection for User Service."""
import redis.asyncio as redis
from typing import Optional
from app.core.config import REDIS_URL

_redis_client: Optional[redis.Redis] = None


async def get_redis() -> redis.Redis:
    """获取 Redis 客户端"""
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    return _redis_client


async def close_redis():
    """关闭 Redis 连接"""
    global _redis_client
    if _redis_client:
        await _redis_client.close()
        _redis_client = None


class RedisKeys:
    """Redis 键名管理"""

    # Token 黑名单
    TOKEN_BLACKLIST = "token:blacklist:{token_hash}"

    # 用户缓存
    USER_CACHE = "user:cache:{user_id}"
    USER_SESSION = "user:session:{user_id}"

    # 登录限流
    LOGIN_RATE_LIMIT = "auth:login:{ip}"

    # 家长验证码
    PARENT_VERIFY_CODE = "parent:verify:{student_id}"

    @staticmethod
    def token_blacklist(token_hash: str) -> str:
        return RedisKeys.TOKEN_BLACKLIST.format(token_hash=token_hash)

    @staticmethod
    def user_cache(user_id: str) -> str:
        return RedisKeys.USER_CACHE.format(user_id=user_id)

    @staticmethod
    def user_session(user_id: str) -> str:
        return RedisKeys.USER_SESSION.format(user_id=user_id)

    @staticmethod
    def login_rate_limit(ip: str) -> str:
        return RedisKeys.LOGIN_RATE_LIMIT.format(ip=ip)

    @staticmethod
    def parent_verify_code(student_id: str) -> str:
        return RedisKeys.PARENT_VERIFY_CODE.format(student_id=student_id)