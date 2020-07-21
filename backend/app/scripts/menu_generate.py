import sqlalchemy
"""
    用于生成vue-element-admin的菜单内容
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,backref

from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



url = "mysql://root:wzx940516@49.235.242.224/DWDB?charset=utf8"
engine = create_engine(url)
data = [
                     {"path": "/permission", "component": "#",
                      "redirect": "/permission/index", "alwaysShow": True,
                      "meta": {"title": "权限测试页", "icon": "lock", "roles": ["admin", "editor"]},
                      "children": [{"path": "page", "component": "views/permission/page",
                                    "name": "PagePermission",
                                    "meta": {"title": "页面权限", "roles": ["admin"]}},
                                   {"path": "directive", "component": "views/permission/directive",
                                    "name": "DirectivePermission",
                                    "meta": {"title": "指令权限"}},
                                   {"path": "role", "component": "views/permission/role",
                                    "name": "RolePermission",
                                    "meta": {"title": "角色权限", "roles": ["admin"]}}]},
                     {"path": "external-link", "component": "layout/Layout", "children": [
                         {"path": "https://github.com/PanJiaChen/vue-element-admin",
                          "meta": {"title": "External Link", "icon": "link"}}]},
    ]


class Menu(Base):
    """
    菜单表
    """
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(32),doc="唯一标识用于页面缓存" )
    path = Column(String(128),doc="路由")
    component = Column(String(32),)
    hidden = Column(Boolean(), default=False)
    alwaysShow = Column(Boolean(),default=False)#是否永久展示一级菜单
    redirect = Column(String(32),)
    #meta
    title = Column(String(32),)
    icon = Column(String(32),)
    noCache = Column(Boolean(),default=True,doc="是否缓存")
    affix = Column(Boolean(),default=False,doc = "固钉")
    order = Column(Integer,doc = "排序")
    parent_id = Column(Integer,index=True,)
    remark = Column(String(256), doc = "备注")

def deal_menu(menu,parent_id  = None):
    if "children" in menu:children = menu.pop("children")
    else:children = False
    if "meta" in menu:
        meta = menu.pop("meta")
        menu.update(meta)
    if "roles" in menu:
        roles = menu.pop("roles")
    menu = Menu(**menu)
    menu.parent_id = parent_id
    session.add(menu)
    session.commit()
    if children:
        for child in children:
            deal_menu(child,menu.id)



if __name__ == '__main__':
    session = sessionmaker(bind=engine)
    session = session()
    menus = session.query(Menu).all()
    for m in menus:
        if m.parent_id is not None:
            try:
                session.query(Menu).filter(Menu.id==m.id).delete()
            except Exception as e:
                pass
    for m in menus:
        if m.parent_id is not None:
            try:
                session.query(Menu).filter(Menu.id==m.id).delete()
            except Exception as e:
                pass
    for m in menus:
        if m.parent_id is not None:
            try:
                session.query(Menu).filter(Menu.id==m.id).delete()
            except Exception as e:
                pass
    session.query(Menu).delete()
    session.commit()
    for menu in data:
        deal_menu(menu)
    session.commit()
    session.query(Menu).filter(Menu.component == "layout/Layout").update({"component": "#"})
    session.commit()
