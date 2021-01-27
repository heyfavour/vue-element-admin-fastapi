from typing import Optional, Any

from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: str
    order: Optional[str] = None
    routes: Any = None


# Properties to receive on item creation
class RoleCreate(RoleBase):
    pass


# Properties to receive on item update
class RoleUpdate(RoleBase):
    pass
