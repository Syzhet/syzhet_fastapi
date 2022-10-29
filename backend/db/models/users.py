from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

from ..base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, unique=True)
    username = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(
        DateTime(),
        default=datetime.now,
        onupdate=datetime.now
    )
    is_admin = Column(Boolean(), default=False)
    orders = relationship("Order", backref='user')

    def __str__(self):
        return f'id: {self.id}, first_name: {self.first_name}'
