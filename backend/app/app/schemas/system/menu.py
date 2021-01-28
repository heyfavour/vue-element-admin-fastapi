from typing import Optional
from pydantic import BaseModel


# Shared properties
class MenuBase(BaseModel):
    path: str = ""
    component: Optional[str] = None
    affix: Optional[bool] = False
    external_link: Optional[bool] = False
    parent_id: Optional[int] = None

    name: Optional[str] = None
    title: str = ""
    icon: str = ""
    no_cache: bool = False
    order: int = 0


# Properties to receive on item creation
class MenuCreate(MenuBase):
    pass


# Properties to receive on item update
class MenuUpdate(MenuBase):
    id: int
