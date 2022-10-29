from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    updated_on: datetime

    class Config:
        orm_mode = True
