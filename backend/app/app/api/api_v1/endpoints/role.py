from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException,Body
from sqlalchemy.orm import Session,joinedload_all,contains_eager,Load
from fastapi.encoders import jsonable_encoder
from app import crud, models, schemas
from app.api import deps
from app.utils import deal_menus

router = APIRouter()



def menus_to_list(menus):
    """菜单dict生成list"""
    if menus.get("children", []) == []:return [menus,]
    children = [menus_to_list(menu)[0] for menu in menus['children']]
    menus.pop("children")
    menus = [menus,]
    menus.extend(children)
    return menus


@router.get("/routes", response_model=schemas.Response)
def routes(db: Session = Depends(deps.get_db),current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    menus = db.query(models.Menu).options(joinedload_all(models.Menu.children,models.Menu.roles)).filter(models.Menu.parent_id == None
            ).order_by(models.Menu.order.asc()).all()
    menus = [deal_menus(menu) for menu in menus]
    return {"code": 20000,"data": menus}


@router.get("/roles", response_model=schemas.Response)
def read_roles(db: Session = Depends(deps.get_db),current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data
    """
    #目前只支持二级菜单，递归想不到漂亮的写法
    role_infos = {}
    roles = db.query(models.Role).all()
    for role in roles:
        role_infos[role.key] = {"key": role.key, "name": role.name, "description": role.description,"routes":[]}
    roles = db.query(models.Role,models.Menu
                      ).join(models.Role_Menu, models.Role_Menu.role_id == models.Role.id
                      ).join(models.Menu, models.Menu.id == models.Role_Menu.menu_id
                      ).order_by(models.Role.id.asc(),models.Menu.parent_id.asc(),models.Menu.id.asc()).all()
    for role in roles:
        if role.Menu.parent_id is None:role_infos[role.Role.key]["routes"].append(role.Menu.dict())
    for role,role_info in role_infos.items():
        for i,parent_menu in enumerate(role_info["routes"]):
            children = [m.Menu.dict() for m in roles if m.Menu.parent_id == parent_menu["id"] and m.Role.key == role]
            if children != []:role_infos[role]["routes"][i]["children"] = children
    role_lists = [i for i in role_infos.values()]
    return {"code": 20000, "data":role_lists}


@router.put("/{id}", response_model=schemas.Response)
def update_roles(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    role_in: schemas.RoleUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve Mock Data
    """
    urole = {"name":role_in.name,"description": role_in.description,}
    role = db.query(models.Role).filter(models.Role.key == id)
    role.update(urole)
    #更新权限菜单 Role_Menu
    role = role.one()
    routes = role_in.routes
    db.query(models.Role_Menu).filter(models.Role_Menu.role_key == id).delete()
    for route in routes:
        role_menu = menus_to_list(route)
        for index,menu in enumerate(role_menu):
            role_menu = {"role_id":role.id,"role_key":role.key,"menu_id":menu['id']}
            db.add(models.Role_Menu(**role_menu))
    return {"code": 20000, "data":{"status":"success"}}


@router.post("/", response_model=schemas.Response)
def create_role(
    *,
    db: Session = Depends(deps.get_db),
    role_in: schemas.RoleCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new Role.
    """
    role = {"key":role_in.key,"name":role_in.name,"description": role_in.description,}
    role = models.Role(**role)
    db.add(role)
    db.flush()
    #更新权限菜单 Role_Menu
    routes = role_in.routes
    db.query(models.Role_Menu).filter(models.Role_Menu.role_key == role.id).delete()
    for route in routes:
        role_menu = menus_to_list(route)
        for index,menu in enumerate(role_menu):
            role_menu = {"role_id":role.id,"role_key":role.key,"menu_id":menu['id']}
            db.add(models.Role_Menu(**role_menu))
    return {"code": 20000, "data": {"key":role_in.key}}

@router.delete("/{id}", response_model=schemas.Response)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    db.query(models.Role_Menu).filter(models.Role_Menu.role_key == id).delete()
    db.query(models.Role).filter(models.Role.key == id).delete()

    return {"code": 20000, "data":{"status":"success"}}
