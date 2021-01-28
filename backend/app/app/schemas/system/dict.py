from typing import Optional

from pydantic import BaseModel


# Shared properties
class DictTypeBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None


# Properties to receive on item creation
class DictTypeCreate(DictTypeBase):
    pass


# Properties to receive on item update
class DictTypeUpdate(DictTypeBase):
    id: int


class DictDataBase(BaseModel):
    """字典明细"""
    label: str
    order: int
    remark: Optional[str] = None
    type_id: str
    css_class: Optional[str] = None
    list_class: Optional[str] = None
    is_default: Optional[bool] = None


class DictDataCreate(DictDataBase):
    pass


class DictDataUpdate(DictDataBase):
    id: int
