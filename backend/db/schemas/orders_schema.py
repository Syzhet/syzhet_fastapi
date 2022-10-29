from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    title: str
    description: str


class OrderCreate(OrderBase):
    user_id: str


class UserGet(OrderCreate):
    updated_on: datetime

    class Config:
        orm_mode = True
