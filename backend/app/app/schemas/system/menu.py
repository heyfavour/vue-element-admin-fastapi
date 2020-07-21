from typing import Optional

from pydantic import BaseModel

from typing import Optional

from pydantic import BaseModel


# Shared properties
class MenuBase(BaseModel):
    path : str
    component : str
    hidden :bool
    menu_type : str
    external_link :bool
    parent_id: Optional[int] = None
    #meta
    name : str
    title : str
    icon : str
    noCache :bool
    order :int
    parent_id:Optional[int] = None


# Properties to receive on item creation
class MenuCreate(MenuBase):
    pass


# Properties to receive on item update
class MenuUpdate(MenuBase):
    id: int
    alwaysShow :bool
    redirect : Optional[str] = None
    affix :bool


# Properties shared by models stored in DB
class MenuInDBBase(MenuBase):
    pass


# Properties to return to client
class Menu(MenuInDBBase):
    pass


# Properties properties stored in DB
class MenuInDB(MenuInDBBase):
    pass
