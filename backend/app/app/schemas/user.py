from typing import Optional,List

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username : str
    nickname : str
    sex:str
    identity_card :str
    phone :Optional[str] = None
    address :Optional[str] = None
    work_start :Optional[str] = None
    status :Optional[str] = None
    hashed_password :Optional[str] = None
    avatar :Optional[str] = None
    introduction :Optional[str] = None

    is_active :Optional[bool] = None
    is_superuser :Optional[bool] = None




# Properties to receive via API on creation
class UserCreate(UserBase):
    pass


# Properties to receive via API on update
class UserUpdate(UserBase):
    id: Optional[int] = None
    deptId:Optional[int] = None
    postIds:List[int] = []
    roleIds:List[int] = []
