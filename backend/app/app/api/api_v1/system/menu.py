from typing import Any, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps
from app.extensions.utils import list_to_tree

router = APIRouter()


@router.get("/routes", response_model=schemas.Response)
def read_routes(title: Optional[str] = None, db: Session = Depends(deps.get_db)) -> Any:
    """菜单管理-查询"""
    menus = db.query(models.Menu)
    if title: menus = menus.filter(models.Menu.title.like('%' + title + '%'))  # 暂时前端不进行title查询，前端不知道如何展示
    menus = menus.all()
    menus = list_to_tree([menu.dict() for menu in menus], order="order")
    return {"code": 20000, "data": menus}


@router.get("/{menu_id}", response_model=schemas.Response)
def read_menu_id(menu_id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Get a specific menu by id."""
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).one()
    return {"code": 20000, "data": menu, }


@router.put("/", response_model=schemas.Response)
def update_menu(*, db: Session = Depends(deps.get_db), menu_in: schemas.MenuUpdate) -> Any:
    """update a specific menu by id."""
    db.query(models.Menu).filter(models.Menu.id == menu_in.id).update(menu_in)
    return {"code": 20000, "data": "", "message": "修改成功", }


@router.delete("/{menu_id}", response_model=schemas.Response)
def delete_menu_id(menu_id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """Delete a specific menu by id."""
    db.query(models.Menu).filter(models.Menu.id == menu_id).delete()
    return {"code": 20000, "data": "", "message": f"删除成功"}


@router.post("/", response_model=schemas.Response)
def post_menu(*, db: Session = Depends(deps.get_db), menu: schemas.MenuCreate, ) -> Any:
    """Add a specific menu"""
    db.add(models.Menu(**menu.dict()))
    return {"code": 20000, "data": "", "message": "新增菜单成功"}
