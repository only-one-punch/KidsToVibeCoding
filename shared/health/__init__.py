"""健康检查模块"""
from fastapi import APIRouter, Response
from typing import Optional
import time

router = APIRouter(tags=["health"])

# 服务启动时间
_start_time = time.time()

@router.get("/health")
async def health_check() -> dict:
    """健康检查端点"""
    return {
        "status": "healthy",
        "uptime": round(time.time() - _start_time, 2)
    }

@router.get("/health/ready")
async def readiness_check() -> dict:
    """就绪检查端点 - 可扩展检查数据库、Redis 等连接"""
    return {"status": "ready"}

@router.get("/health/live")
async def liveness_check() -> dict:
    """存活检查端点"""
    return {"status": "alive"}
