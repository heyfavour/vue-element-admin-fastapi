from fastapi import APIRouter, Depends

from app.api import deps
from app.api.api_v1 import endpoints
from app.api.api_v1 import system
from app.api.api_v1 import report

api_router = APIRouter()

api_router.include_router(endpoints.login_router)#登录另起一个路由避免全局dependencies

# 各自模块的路由由各自模块负责
api_router.include_router(endpoints.router,dependencies=[Depends(deps.get_current_active_user)])
api_router.include_router(system.router,dependencies=[Depends(deps.get_current_active_user)])
api_router.include_router(report.router,dependencies=[Depends(deps.get_current_active_user)])
