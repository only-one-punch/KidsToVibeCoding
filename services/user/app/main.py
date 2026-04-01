"""User Service - FastAPI Application."""
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CodeBuddyAI - User Service",
    description="用户认证与档案管理服务",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
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
