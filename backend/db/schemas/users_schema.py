from datetime import datetime

from pydantic import BaseConfig, BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    telegram_id: int


class UserGet(UserCreate):
    id: int
    updated_on: datetime

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        orm_mode = True
