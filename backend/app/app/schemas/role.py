from typing import Optional,Any

from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    key: Optional[str] = None
    name : Optional[str] = None
    description : str
    routes: Any = None


# Properties to receive on item creation
class RoleCreate(RoleBase):
    pass


# Properties to receive on item update
class RoleUpdate(RoleBase):
    pass


# Properties shared by models stored in DB
class RoleInDBBase(RoleBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Role(RoleInDBBase):
    pass


# Properties properties stored in DB
class RoleInDB(RoleInDBBase):
    pass
