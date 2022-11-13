from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    telegram_id: int


class UserOrder(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class UserWithOrder(UserCreate):
    id: int
    updated_on: datetime
    orders: List[UserOrder]

    class Config:
        orm_mode = True


class UserGet(UserCreate):
    id: int
    updated_on: datetime

    class Config:
        orm_mode = True
