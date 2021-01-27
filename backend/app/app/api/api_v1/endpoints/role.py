from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from app import models, schemas
from app.api import deps
from app.extensions.utils import list_to_tree, dfs_tree_to_list

router = APIRouter()


@router.get("/routes", response_model=schemas.Response)
def routes(db: Session = Depends(deps.get_db)) -> Any:
    """get all routes info"""
    menus = db.query(models.Menu).options(joinedload(models.Menu.role_menu)).all()

    def deal_menu(menu):
        meta = {'title': menu.title,
                "icon": menu.icon,
                "noCache": menu.no_cache,
                "affix": menu.affix,
                "order": menu.order,
                "roles": [role.role_id for role in menu.role_menu]
                }
        menu = menu.dict()
        # menu["hidden"] = False
        # menu["alwaysShow"] = True
        menu['meta'] = meta
        return menu

    menus = list_to_tree([deal_menu(menu) for menu in menus], order="order")
    return {"code": 20000, "data": menus}


@router.get("/roles", response_model=schemas.Response)
def read_roles(db: Session = Depends(deps.get_db)) -> Any:
    """角色权限"""
    role_infos = []

    def deal_menu(menu):
        meta = {'title': menu.title, }
        menu = menu.dict()
        menu['meta'] = meta
        return menu

    # 先取出所有数据再组成树结构
    roles = db.query(models.Role).options(joinedload(models.Role.role_menu).joinedload(models.Role_Menu.role)).order_by(
        models.Role.order.asc()).all()
    for role in roles:
        role_menus_list = list_to_tree([deal_menu(role_menu.menu) for role_menu in role.role_menu], order="order")
        role_info = {
            "id": role.id,
            "name": role.name,
            "description": role.description,
            "order": role.order,
            "routes": role_menus_list
        }
        role_infos.append(role_info)
    return {"code": 20000, "data": role_infos}


@router.put("/{id}", response_model=schemas.Response)
def update_role(*, db: Session = Depends(deps.get_db), id: str, role_in: schemas.RoleUpdate, ) -> Any:
    """角色权限 confirm"""
    urole = {"name": role_in.name, "description": role_in.description, "order": role_in.order}
    role = db.query(models.Role).filter(models.Role.id == id)
    role.update(urole)
    # 删除原有菜单
    db.query(models.Role_Menu).filter(models.Role_Menu.role_id == id).delete()
    # 新增现有菜单
    menus_list = dfs_tree_to_list(role_in.routes)
    menus_list = [models.Role_Menu(**{"role_id": role.one().id, "menu_id": menu_id}) for menu_id in menus_list]
    db.bulk_save_objects(menus_list)
    return {"code": 20000, "data": {"status": "success"}}


@router.post("/", response_model=schemas.Response)
def create_role(*, db: Session = Depends(deps.get_db), role_create: schemas.RoleCreate, ) -> Any:
    """
    ADD new Role.
    """
    # ROLE
    role = {"name": role_create.name, "description": role_create.description, "order": role_create.order}
    role = models.Role(**role)
    db.add(role)
    db.flush()
    # ROLE_MENU
    menus_list = dfs_tree_to_list(role_create.routes)
    menus_list = [models.Role_Menu(**{"role_id": role.id, "menu_id": menu_id}) for menu_id in menus_list]
    db.bulk_save_objects(menus_list)
    return {"code": 20000, "data": {"id": role.id}}


@router.delete("/{id}", response_model=schemas.Response)
def delete_role(*, db: Session = Depends(deps.get_db), id: str, ) -> Any:
    """
    Delete an Role.
    """
    db.query(models.Role_Menu).filter(models.Role_Menu.role_id == id).delete()
    db.query(models.Role).filter(models.Role.id == id).delete()

    return {"code": 20000, "data": {"status": "success"}}
