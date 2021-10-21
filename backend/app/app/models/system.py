from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Date
from sqlalchemy.orm import relationship, backref
import datetime
from app.db.base_class import Base
"""
relationship 自引用加入remote_side use_list=False -> one-to-one 默认use_list=True
"""

class Dict_Type(Base):
    """数据字典"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(32), doc="字典编码")
    name = Column(String(32), doc="字典名称")
    description = Column(String(512), doc="备注")

    data = relationship("Dict_Data", backref="type")


class Dict_Data(Base):
    """字典明细"""
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String(128))
    order = Column(Integer)
    remark = Column(String(512))
    type_id = Column(Integer, ForeignKey("dict_type.id", ondelete='CASCADE'))
    # meta
    css_class = Column(String(128), default="", doc="css样式")
    list_class = Column(String(128), default="", doc="表格样式")
    is_default = Column(Boolean(), default=False, doc="是否默认 ")


class Department(Base):
    """部门表"""
    # __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(128), doc="部门代码")
    name = Column(String(128), doc="部门名称")
    order = Column(Integer, doc="排序")
    parent_id = Column(Integer, ForeignKey("department.id", ondelete='CASCADE'), index=True, nullable=True)
    status = Column(Boolean, doc="当前有效")
    start_date = Column(Date, default=datetime.date.today())
    end_date = Column(Date, default='3000-12-31')

    children = relationship('Department', order_by=order.asc(),
                                backref=backref('parent',uselist=False,remote_side=[id]))


class Menu(Base):
    """ 菜单表"""
    # __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String(128), doc="路由")
    component = Column(String(32), doc="组件", default="")
    # hidden = Column(Boolean(), default=False)
    # always_show = Column(Boolean(),default=True)
    # redirect = Column(String(32),default="noRedirect",doc = "当设置 noRedirect 的时候该路由在面包屑导航中不可被点击")
    external_link = Column(Boolean, doc="是否外链", default=True)
    # meta
    name = Column(String(32), doc="唯一标识用于页面缓存，否则keep-alive会出问题")  # index组件的name
    title = Column(String(32), doc="标题")
    icon = Column(String(32), doc="小图标")
    no_cache = Column(Boolean(), default=False, doc="是否缓存")
    affix = Column(Boolean(), default=False, doc="固钉")
    order = Column(Integer, doc="排序")
    parent_id = Column(Integer, ForeignKey("menu.id", ondelete='CASCADE'), index=True,
                       nullable=True, )  # ondelete='CASCADE' 联级删除

    parent = relationship('Menu', remote_side=[id],uselist=False,order_by=order.asc(),
                          backref=backref('children'))
    role_menu = relationship("Role_Menu", backref="menu")
