from typing import Optional, Any

from pydantic import BaseModel


# Shared properties
class Response(BaseModel):
    code: Optional[int] = None
    data : Optional[Any] = None
    message: Optional[str] = None
