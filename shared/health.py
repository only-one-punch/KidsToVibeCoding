"""
健康检查模块
各服务共用
"""
from datetime import datetime
from typing import Dict, Any, Optional
from fastapi import Response
from pydantic import BaseModel


class HealthStatus(BaseModel):
    """健康检查响应模型"""
    status: str
    service: str
    timestamp: str
    version: str = "0.1.0"
    dependencies: Dict[str, str] = {}


def create_health_response(
    service_name: str,
    dependencies: Optional[Dict[str, str]] = None,
    is_healthy: bool = True
) -> Dict[str, Any]:
    """创建健康检查响应"""
    return {
        "status": "healthy" if is_healthy else "unhealthy",
        "service": service_name,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "0.1.0",
        "dependencies": dependencies or {}
    }


async def check_database(db_url: str) -> str:
    """检查数据库连接"""
    # TODO: 实际数据库连接检查
    return "connected"


async def check_redis(redis_url: str) -> str:
    """检查 Redis 连接"""
    # TODO: 实际 Redis 连接检查
    return "connected"
