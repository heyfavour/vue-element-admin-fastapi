from pydantic import BaseModel
from pydantic.networks import EmailStr

class Msg(BaseModel):
    msg: str

class Email(BaseModel):
    email: EmailStr
