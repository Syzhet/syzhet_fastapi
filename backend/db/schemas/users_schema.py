from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    telegram_id: int


class UserGet(UserCreate):
    id: int
    updated_on: datetime

    class Config:
        orm_mode = True
