from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship,backref

from app.db.base_class import Base

class Menu(Base):
    """
    菜单表
    """
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    path = Column(String(128),doc="路由")
    component = Column(String(32),)
    hidden = Column(Boolean(), default=False)
    alwaysShow = Column(Boolean(),default=False)#是否永久展示一级菜单
    redirect = Column(String(32),)
    menu_type = Column(String(32),doc = "M目录 C 菜单 F 按钮" ,default="C")
    external_link = Column(Boolean,doc = "是否外链",default=True)
    #meta
    name = Column(String(32),doc="唯一标识用于页面缓存" )
    title = Column(String(32),)
    icon = Column(String(32),)
    noCache = Column(Boolean(),default=True,doc="是否缓存")
    affix = Column(Boolean(),default=False,doc = "固钉")
    order = Column(Integer,doc = "排序")
    parent_id = Column(Integer, ForeignKey("menu.id"),index=True,)

    parent = relationship('Menu', uselist=True, remote_side=[id], backref=backref('children', uselist=True))
    roles = relationship("Role_Menu", backref="menus")

    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns if getattr(self, c.name, None) != None}

class Role(Base):
    """权限组"""
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    key = Column(String(32), nullable=False)
    name = Column(String(32), )
    description = Column(String(128), )

class Role_Menu(Base):
    """权限组-菜单-中间表"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    role_key = Column(String(32))
    menu_id = Column(Integer, ForeignKey("menu.id"))
