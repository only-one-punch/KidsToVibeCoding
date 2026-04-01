"""AI Assistant Service - AI 对话服务"""
from fastapi import FastAPI

app = FastAPI(
    title="CodeBuddyAI AI Assistant",
    description="AI 对话服务",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {
        "status": "healthy",
        "service": "ai-assistant",
        "version": "0.1.0"
    }


@app.get("/")
async def root():
    return {"service": "ai-assistant", "docs": "/docs"}
