import datetime

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    """用户表"""
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False, doc="编码")
    nickname = Column(String(32), doc="姓名")
    sex = Column(String(8), doc="性别")
    identity_card = Column(String(32), doc="身份证")
    phone = Column(String(32), doc="手机号")
    address = Column(String(32), doc="地址")
    work_start = Column(Date, doc="入职日期", default=datetime.datetime.today())
    hashed_password = Column(String(128), nullable=False, doc="密码")
    avatar = Column(String(128), doc="头像")
    introduction = Column(String(256), doc="自我介绍")
    status = Column(String(32), nullable=False, doc="状态")
    is_active = Column(Boolean(), default=True, doc="是否活跃")
    is_superuser = Column(Boolean(), default=False, doc="是否超级管理员")

    user_role = relationship("User_Role", backref="user")
    user_department = relationship("User_Department", backref="user")
    user_dict = relationship("User_Dict", backref="user")


class User_Role(Base):
    """用户-权限组-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'))
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role")


class User_Department(Base):
    """用户-部门-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'))
    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department")


class User_Dict(Base):
    """用户-字典-中间表"""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'))
    dict_id = Column(Integer, ForeignKey("dict_data.id",ondelete='CASCADE'))

    dict_data = relationship("Dict_Data", backref="user_dict")

