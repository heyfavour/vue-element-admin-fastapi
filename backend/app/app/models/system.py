from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,DateTime,Date
from sqlalchemy.orm import relationship,backref
import datetime
from app.db.base_class import Base



class Dict_Type(Base):
    """数据字典"""
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    code = Column(String(32))
    name = Column(String(32))
    description = Column(String(512), index=True)

    data = relationship("Dict_Data", backref="type")


class Dict_Data(Base):
    """字典明细"""
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    label = Column(String(128))
    order = Column(Integer)
    remark = Column(String(512))

    type_id = Column(Integer,ForeignKey("dict_type.id"))
    css_class = Column(String(128),default="",doc="css样式")
    list_class = Column(String(128),default="",doc="表格样式")
    is_default = Column(Boolean(),default=False,doc="是否默认 ")


class Department(Base):
    """部门表"""
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    code = Column(String(128), doc="部门代码")
    name = Column(String(128), doc="部门名称")
    order = Column(Integer,doc="排序")
    parent_id = Column(Integer, ForeignKey("department.id"),index=True,nullable=True)
    status = Column(Boolean, doc="当前有效")
    start_date = Column(Date, default=datetime.date.today())
    end_date = Column(Date, default='3000-12-31')

    children = relationship('Department', uselist=True,order_by=order.asc(), backref=backref('parent', uselist=True,remote_side=[id]))


class Menu(Base):
    """ 菜单表"""
    __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    path = Column(String(128),doc="路由")
    component = Column(String(32),)
    hidden = Column(Boolean(), default=False)
    always_show = Column(Boolean(),default=False)
    redirect = Column(String(32),)
    menu_type = Column(String(32),doc = "M目录 C 菜单 F 按钮" ,default="C")
    external_link = Column(Boolean,doc = "是否外链",default=True)
    #meta
    name = Column(String(32),doc="唯一标识用于页面缓存" )
    title = Column(String(32),)
    icon = Column(String(32),)
    no_cache = Column(Boolean(),default=True,doc="是否缓存")
    affix = Column(Boolean(),default=False,doc = "固钉")
    order = Column(Integer,doc = "排序")
    parent_id = Column(Integer, ForeignKey("menu.id"),index=True,nullable=True)

    parent = relationship('Menu', uselist=True, remote_side=[id], backref=backref('children', uselist=True))
    roles = relationship("Role_Menu", backref="menus")

    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns if getattr(self, c.name, None) != None}
