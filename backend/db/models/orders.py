from datetime import datetime

from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship

from ..base import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))
    updated_on = Column(DateTime(), default=datetime.now)
    user = relationship("User", backref='orders')

    def __str__(self):
        return f'id: {self.id}, title: {self.title}'
