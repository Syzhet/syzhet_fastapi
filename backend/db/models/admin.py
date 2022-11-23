from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from ..base import Base


class Admin(Base):
    """Сlass for representing a admin in database."""

    __tablename__ = 'admins'

    id = Column(Integer(), primary_key=True, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(200), nullable=False)
    created_on = Column(DateTime(), server_default=func.now())
    updated_on = Column(
        DateTime(),
        server_default=func.now(),
        server_onupdate=func.now()
    )

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'id: {self.id}, username: {self.username}'
