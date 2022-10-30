from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func

from ..base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, unique=True)
    telegram_id = Column(Integer(), nullable=False, unique=True)
    username = Column(String(100), nullable=False)
    created_on = Column(DateTime(), server_default=func.now())
    updated_on = Column(
        DateTime(),
        server_default=func.now(),
        server_onupdate=func.now()
    )
    is_admin = Column(Boolean(), default=False)

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'id: {self.id}, username: {self.username}'
