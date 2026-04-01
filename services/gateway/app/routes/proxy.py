"""代理路由模块 - 转发请求到后端服务"""
import httpx
from fastapi import APIRouter, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from typing import Optional

from ..config import SERVICES

router = APIRouter()


async def proxy_request(
    request: Request,
    service_name: str,
    path: str,
) -> Response:
    """通用 HTTP 请求代理"""
    service = SERVICES.get(service_name)
    if not service:
        return Response(status_code=404, content=f"Service {service_name} not found")
    
    url = f"{service.base_url}/{path}"
    
    # 转发 headers（排除 Host）
    headers = dict(request.headers)
    headers.pop("host", None)
    
    # 获取请求体
    body = await request.body()
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=body,
            params=request.query_params,
        )
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
    )


# User Service 路由
@router.api_route("/api/v1/user/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_user(request: Request, path: str):
    """转发到 User Service"""
    return await proxy_request(request, "user", f"api/v1/user/{path}")


# Learning Service 路由
@router.api_route("/api/v1/learning/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_learning(request: Request, path: str):
    """转发到 Learning Service"""
    return await proxy_request(request, "learning", f"api/v1/learning/{path}")


# AI Assistant Service 路由
@router.api_route("/api/v1/chat/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_chat(request: Request, path: str):
    """转发到 AI Assistant Service"""
    return await proxy_request(request, "ai-assistant", f"api/v1/chat/{path}")


# Multimodal Service 路由
@router.api_route("/api/v1/voice/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_voice(request: Request, path: str):
    """转发到 Multimodal Service"""
    return await proxy_request(request, "multimodal", f"api/v1/voice/{path}")


# Sandbox Service 路由
@router.api_route("/api/v1/code/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_code(request: Request, path: str):
    """转发到 Sandbox Service"""
    return await proxy_request(request, "sandbox", f"api/v1/code/{path}")
