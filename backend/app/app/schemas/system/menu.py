from typing import Optional

from pydantic import BaseModel

from typing import Optional

from pydantic import BaseModel


# Shared properties
class MenuBase(BaseModel):
    path : str
    hidden :bool
    menu_type : str


    title : str
    icon : str
    no_cache :bool
    order :int



# Properties to receive on item creation
class MenuCreate(MenuBase):
    pass


# Properties to receive on item update
class MenuUpdate(MenuBase):
    id: int
    always_show :bool
    redirect : Optional[str] = None
    affix :Optional[bool] = False
    parent_id:Optional[int] = None
    external_link :Optional[bool] = False
    component : Optional[str] = None
    #meta
    name : Optional[str] = None


