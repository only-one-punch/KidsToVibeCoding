"""AI Assistant Service - FastAPI Application."""
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CodeBuddyAI - AI Assistant", version="0.1.0", docs_url="/docs")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "service": "ai-assistant-service", "timestamp": datetime.utcnow().isoformat() + "Z", "version": "0.1.0"}

@app.get("/ready", tags=["Health"])
async def readiness_check():
    return {"status": "ready"}
