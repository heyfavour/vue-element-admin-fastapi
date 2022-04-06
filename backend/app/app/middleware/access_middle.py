import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.extensions.logger import backend_logger


class AccessMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        backend_logger.info(f"{request.client.host} {request.method} {request.url}  [I]")
        try:
            response = await call_next(request)
        except Exception as exc:
            backend_logger.exception(exc)
            raise exc
        backend_logger.info(f"{request.client.host} {request.method} {request.url}  [0]")
        return response
