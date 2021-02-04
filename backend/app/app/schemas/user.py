import datetime

from typing import Optional, List
from pydantic import BaseModel

from app.core.security import get_password_hash
from app.core.config import settings


# Shared properties
class UserBase(BaseModel):
    username: str
    nickname: str
    sex: str
    identity_card: str
    phone: Optional[str] = None
    # address: Optional[str] = None
    work_start: Optional[str] = datetime.datetime.today()
    status: Optional[str] = None
    hashed_password: str = get_password_hash(settings.INIT_PASSWORD)
    # avatar: Optional[str] = None
    introduction: Optional[str] = None
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    deptId: Optional[int] = None
    postIds: List[int] = []
    roleIds: List[int] = []


# Properties to receive via API on update
class UserUpdate(UserBase):
    id: Optional[int] = None
    deptId: Optional[int] = None
    postIds: List[int] = []
    roleIds: List[int] = []


# reset password
class UserPWReset(BaseModel):
    user_id: int
    password: str
