from pydantic import BaseModel


class Msg(BaseModel):
    receiver_emal: str
