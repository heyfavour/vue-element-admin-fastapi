from fastapi import APIRouter
from app.api.api_v1.system import menu,dict,department,user

router = APIRouter()
router.include_router(user.router, prefix="/system/user", tags=["system"])
router.include_router(menu.router, prefix="/system/menu", tags=["system"])
router.include_router(dict.router, prefix="/system/dict", tags=["system"])
router.include_router(department.router, prefix="/system/department", tags=["system"])

