import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.extensions.logger import backend_logger


class AccessMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.datetime.now()
        response = await call_next(request)
        end_time = datetime.datetime.now()
        backend_logger.info(
            f"{request.client.host} {request.method} {request.url} {response.status_code} {end_time - start_time}"
        )
        return response
