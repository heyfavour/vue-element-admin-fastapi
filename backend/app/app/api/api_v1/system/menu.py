from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException,Body,Request
from sqlalchemy.orm import Session,joinedload_all,contains_eager,Load
from fastapi.encoders import jsonable_encoder
from app import crud, models, schemas
from app.api import deps
from app.utils import deal_menus


router = APIRouter()
@router.get("/routes", response_model=schemas.Response)
def read_routes(name: Optional[str] = None, hidden: Optional[bool] = None, db: Session = Depends(deps.get_db),
                current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    """
    Retrieve Mock Data.
    """
    menus = db.query(models.Menu).options(joinedload_all(models.Menu.children,models.Menu.roles)).filter(models.Menu.parent_id == None
            ).order_by(models.Menu.order).all()
    menus = [deal_menus(menu) for menu in menus]
    return {"code": 20000,"data": menus}

@router.get("/{menu_id}", response_model=schemas.Response)
def read_menu_id(menu_id: int,current_user: models.User = Depends(deps.get_current_active_user), db: Session = Depends(deps.get_db),) -> Any:
    """
    Get a specific menu by id.
    """
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).one()
    if menu.parent_id is None:menu.parent_id = 0
    return {"code": 20000,"data": menu,"message":"",}

@router.put("", response_model=schemas.Response)
def update_menu(*,db: Session = Depends(deps.get_db),menu_in: schemas.MenuUpdate,
                # current_user: models.User = Depends(deps.get_current_active_user),
                ) -> Any:
    """
    Get a specific menu by id.
    """
    #目录菜单组件放#
    menu_in.alwaysShow = False
    if menu_in.menu_type == "M":
        menu_in.component = "#"
        menu_in.alwaysShow = True
    #ruoyi 在菜单展示的时候加了一个主目录 会需要parent_id
    if menu_in.parent_id == 0:menu_in.parent_id = None
    db.query(models.Menu).filter(models.Menu.id == menu_in.id).update(menu_in)
    db.commit()
    return {"code": 20000,"data": "","message":"修改成功",}

@router.delete("/{menu_id}", response_model=schemas.Response)
def read_menu_id(menu_id: int,current_user: models.User = Depends(deps.get_current_active_user), db: Session = Depends(deps.get_db),) -> Any:
    """
    Get a specific menu by id.
    """
    roles = db.query(models.Role_Menu).filter(models.Role_Menu.menu_id == menu_id).delete()
    menu = db.query(models.Menu).filter(models.Menu.id == menu_id).delete()
    db.commit()
    return {"code": 20000,"data": "","message":"删除成功。删除了{n}个菜单".format(n=menu)}


@router.post("", response_model=schemas.Response)
def post_menu(*, db: Session = Depends(deps.get_db),
                    menu: schemas.MenuCreate,
                    current_user: models.User = Depends(deps.get_current_active_user)
                    ) -> Any:
    """
    Get a specific menu by id.
    """
    db.add(models.Menu(**jsonable_encoder(menu)))
    db.commit()
    return {"code": 20000,"data": "","message":"新增菜单成功"}




