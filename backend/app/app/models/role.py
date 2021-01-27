from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Role(Base):
    """权限组"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(32), doc="权限组名称")
    description = Column(String(128), doc="备注")
    order = Column(Integer, doc="顺序")

    role_menu = relationship("Role_Menu", backref="role")


class Role_Menu(Base):
    """权限组-菜单-中间表"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    menu_id = Column(Integer, ForeignKey("menu.id"))
