
from fastapi import APIRouter

from app.api.api_v1 import endpoints
from app.api.api_v1 import system

api_router = APIRouter()
#各自模块的路由由各自模块负责
api_router.include_router(endpoints.router)
api_router.include_router(system.router)
