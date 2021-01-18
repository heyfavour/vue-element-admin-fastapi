from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String,ForeignKey,DateTime,Date
from sqlalchemy.orm import relationship,backref

from app.db.base_class import Base

import datetime
if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    """
    用户表
    """
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    nickname = Column(String(32))
    sex = Column(String(8),doc = "性别")
    identity_card = Column(String(32),doc="身份证")
    phone = Column(String(32),doc="手机号")
    address = Column(String(32),doc="地址")
    work_start = Column(Date,doc = "入职日期")
    hashed_password = Column(String(128), nullable=False)
    avatar = Column(String(128),doc = "头像")
    introduction = Column(String(256),)
    status = Column(String(32), nullable=False)

    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    roles = relationship("User_Role", backref="user")
    department = relationship("User_Department", backref="user")

class User_Role(Base):
    """用户-权限组-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role")

class User_Department(Base):
    """用户-部门-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department")


class User_Dict(Base):
    """用户-字典-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    dict_id = Column(Integer, ForeignKey("dict_data.id"))

