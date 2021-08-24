import os
# TO SUPPORT RUN python main.py in windows,but I use python "app/main.py" to start in liunx
os.sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.api.api_v1.websocket import socket_app
from app.middleware import register_middleware
from app.extensions.logger import LOGGING_CONFIG

# app
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
# set middleware
register_middleware(app)

# set router
app.include_router(api_router, prefix=settings.API_V1_STR)
# set socketio
app.mount('/', socket_app)

if __name__ == '__main__':
    import uvicorn

    # Don't set debug/reload equals True,becauese TimedRotatingFileHandler can't support multi-prcoess
    # or dont't use my LOGGING_CONFIG in debug/reload
    uvicorn.run(app='main:app', host="0.0.0.0", port=8080, log_config=LOGGING_CONFIG)
