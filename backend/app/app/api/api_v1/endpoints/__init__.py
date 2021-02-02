from fastapi import APIRouter
from app.api.api_v1.endpoints import login, utils, role

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(utils.router, prefix="/utils", tags=["utils"])
router.include_router(role.router, prefix="/role", tags=["role"])
