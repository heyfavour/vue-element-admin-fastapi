from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


class Role(Base):
    """权限组"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(String(32), nullable=False)
    name = Column(String(32), )
    description = Column(String(128), )


class Role_Menu(Base):
    """权限组-菜单-中间表"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    role_key = Column(String(32))
    menu_id = Column(Integer, ForeignKey("menu.id"))
