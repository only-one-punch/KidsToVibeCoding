"""Gateway Service - FastAPI Application."""
import os
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.proxy import create_proxy_router

app = FastAPI(
    title="CodeBuddyAI - Gateway",
    description="API 网关服务",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 服务 URL 配置
SERVICE_URLS = {
    "user": os.getenv("USER_SERVICE_URL", "http://localhost:8001"),
    "learning": os.getenv("LEARNING_SERVICE_URL", "http://localhost:8002"),
    "ai-assistant": os.getenv("AI_ASSISTANT_URL", "http://localhost:8003"),
    "multimodal": os.getenv("MULTIMODAL_URL", "http://localhost:8004"),
    "sandbox": os.getenv("SANDBOX_URL", "http://localhost:8005"),
}

# 注册代理路由
app.include_router(
    create_proxy_router("user", SERVICE_URLS["user"]),
    prefix="/api/v1/user",
    tags=["User Service"]
)
app.include_router(
    create_proxy_router("learning", SERVICE_URLS["learning"]),
    prefix="/api/v1/learning",
    tags=["Learning Service"]
)
app.include_router(
    create_proxy_router("ai-assistant", SERVICE_URLS["ai-assistant"]),
    prefix="/api/v1/chat",
    tags=["AI Assistant"]
)
app.include_router(
    create_proxy_router("multimodal", SERVICE_URLS["multimodal"]),
    prefix="/api/v1/voice",
    tags=["Multimodal Service"]
)
app.include_router(
    create_proxy_router("sandbox", SERVICE_URLS["sandbox"]),
    prefix="/api/v1/code",
    tags=["Sandbox Service"]
)
app.include_router(
    create_proxy_router("multimodal", SERVICE_URLS["multimodal"]),
    prefix="/api/v1/voice",
    tags=["Multimodal Service"]
)
app.include_router(
    create_proxy_router("sandbox", SERVICE_URLS["sandbox"]),
    prefix="/api/v1/code",
    tags=["Sandbox Service"]
)


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "gateway",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "0.1.0",
    }


@app.get("/ready", tags=["Health"])
async def readiness_check():
    return {"status": "ready"}


@app.get("/")
async def root():
    return {"message": "Gateway is running", "docs": "/docs"}
