from datetime import datetime

from pydantic import BaseModel, BaseConfig

from ..schemas.users_schema import UserGet


class OrderBase(BaseModel):
    title: str
    description: str


class OrderCreate(OrderBase):
    user_id: int


class OrderGet(OrderCreate):
    id: int
    updated_on: datetime
    user: UserGet

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        orm_mode = True


class OrderUpdate(OrderBase):
    pass
