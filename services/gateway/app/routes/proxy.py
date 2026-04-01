"""代理路由模块 - 转发请求到后端服务"""
import httpx
from fastapi import APIRouter, Request, Response
from typing import Optional


async def proxy_request(
    request: Request,
    target_url: str,
) -> Response:
    """通用 HTTP 请求代理"""
    # 转发 headers（排除 Host）
    headers = dict(request.headers)
    headers.pop("host", None)

    # 获取请求体
    body = await request.body()

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body,
            params=request.query_params,
        )

    # 过滤响应头
    excluded_headers = {"content-encoding", "transfer-encoding", "connection"}
    response_headers = {
        k: v for k, v in response.headers.items()
        if k.lower() not in excluded_headers
    }

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=response_headers,
        media_type=response.headers.get("content-type"),
    )


def create_proxy_router(service_name: str, base_url: str) -> APIRouter:
    """创建代理路由器"""
    router = APIRouter()

    @router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
    async def proxy(request: Request, path: str):
        """转发请求到后端服务"""
        target_url = f"{base_url}/{path}"
        return await proxy_request(request, target_url)

    return router
