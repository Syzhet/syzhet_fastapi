from datetime import datetime

from pydantic import BaseModel

from .users_schema import UserGet


class OrderBase(BaseModel):
    title: str
    description: str


class OrderCreate(OrderBase):
    user_id: int


class OrderGet(OrderCreate):
    id: int
    updated_on: datetime
    # user: UserGet - для отображения юзера, сделавшего этот заказ

    class Config:
        orm_mode = True
