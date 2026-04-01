"""WebSocket 代理模块"""
import asyncio
import websockets
from fastapi import WebSocket, WebSocketDisconnect
from typing import Optional

from ..config import SERVICES


async def proxy_websocket(
    client_ws: WebSocket,
    service_name: str,
    path: str,
):
    """WebSocket 代理"""
    await client_ws.accept()
    
    service = SERVICES.get(service_name)
    if not service:
        await client_ws.close(code=4004, reason=f"Service {service_name} not found")
        return
    
    # 构建 WebSocket URL
    ws_url = service.base_url.replace("http://", "ws://").replace("https://", "wss://")
    target_url = f"{ws_url}/{path}"
    
    try:
        async with websockets.connect(target_url) as server_ws:
            async def forward_to_server():
                """从客户端转发到服务端"""
                try:
                    while True:
                        data = await client_ws.receive()
                        if "text" in data:
                            await server_ws.send(data["text"])
                        elif "bytes" in data:
                            await server_ws.send(data["bytes"])
                except WebSocketDisconnect:
                    pass
                except Exception:
                    pass
            
            async def forward_to_client():
                """从服务端转发到客户端"""
                try:
                    while True:
                        data = await server_ws.recv()
                        if isinstance(data, str):
                            await client_ws.send_text(data)
                        else:
                            await client_ws.send_bytes(data)
                except Exception:
                    pass
            
            # 并行运行两个转发任务
            await asyncio.gather(
                forward_to_server(),
                forward_to_client(),
            )
    except Exception as e:
        await client_ws.close(code=1011, reason=str(e))
