from typing import Optional

from pydantic import BaseModel

from typing import Optional

from pydantic import BaseModel


# Shared properties
class DepartmentBase(BaseModel):
    code:str
    name:str
    order:int
    parent_id:Optional[int]=None
    status:bool
    start_date:Optional[str]=None
    end_date:Optional[str]=None


# Properties to receive on item creation
class DepartmentCreate(DepartmentBase):
    pass


# Properties to receive on item update
class DepartmentUpdate(DepartmentBase):
    id: int

