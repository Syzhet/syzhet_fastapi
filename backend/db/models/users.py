from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
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
    orders = relationship(
        "Order",
        back_populates='user',
        cascade='save-update, merge, delete',
        lazy='joined'
    )

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'id: {self.id}, username: {self.username}'
