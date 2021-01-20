from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os

os.sys.path.append(os.path.join(os.getcwd(), ".."))

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.api.api_v1.websocket import socket_app
from app.extensions.logger import LOGGING_CONFIG

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
app.mount('/', socket_app)

if __name__ == '__main__':
    import uvicorn

    # Don't set debug/reload as True,becauese TimedRotatingFileHandler can't support multi prcoessing
    # or dont't use my LOGGING_CONFIG
    uvicorn.run(app='main:app', host="0.0.0.0", port=8080, log_config=LOGGING_CONFIG)
