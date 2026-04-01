"""User Service - FastAPI Application."""
import os
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import init_db, close_db
from app.core.redis_client import close_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时初始化
    await init_db()
    yield
    # 关闭时清理
    await close_db()
    await close_redis()


app = FastAPI(
    title="CodeBuddyAI - User Service",
    description="用户认证与档案管理服务",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "user-service",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "0.1.0",
    }


@app.get("/ready", tags=["Health"])
async def readiness_check():
    return {"status": "ready"}


@app.get("/")
async def root():
    return {"message": "User Service is running", "docs": "/docs"}