from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from app.extensions.logger import backend_logger


class AccessMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        backend_logger.info(f"{request.client.host} {request.method} {request.url} {response.status_code}")
        return response
