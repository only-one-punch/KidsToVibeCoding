"""Core configuration for User Service."""
import os
from typing import Optional

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://codebuddy:codebuddy123@localhost:5432/codebuddy")

# Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# JWT
JWT_SECRET = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-in-production")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
JWT_REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# Service
SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "your-service-api-key")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"