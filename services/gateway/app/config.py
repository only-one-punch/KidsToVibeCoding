"""Gateway 服务配置"""
import os
from dataclasses import dataclass


@dataclass
class ServiceConfig:
    """后端服务配置"""
    name: str
    base_url: str
    timeout: float = 30.0


def get_service_configs() -> dict[str, ServiceConfig]:
    """获取所有后端服务配置"""
    return {
        "user": ServiceConfig(
            name="user",
            base_url=os.getenv("USER_SERVICE_URL", "http://localhost:8001"),
        ),
        "learning": ServiceConfig(
            name="learning",
            base_url=os.getenv("LEARNING_SERVICE_URL", "http://localhost:8002"),
        ),
        "ai-assistant": ServiceConfig(
            name="ai-assistant",
            base_url=os.getenv("AI_ASSISTANT_URL", "http://localhost:8003"),
        ),
        "multimodal": ServiceConfig(
            name="multimodal",
            base_url=os.getenv("MULTIMODAL_URL", "http://localhost:8004"),
        ),
        "sandbox": ServiceConfig(
            name="sandbox",
            base_url=os.getenv("SANDBOX_URL", "http://localhost:8005"),
        ),
    }
