"""Learning Service - 学习服务"""
from fastapi import FastAPI

app = FastAPI(
    title="CodeBuddyAI Learning Service",
    description="学习管理服务",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {
        "status": "healthy",
        "service": "learning",
        "version": "0.1.0"
    }


@app.get("/")
async def root():
    return {"service": "learning", "docs": "/docs"}
