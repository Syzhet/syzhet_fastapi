from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..base import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))
    updated_on = Column(DateTime(), server_default=func.now())
    user = relationship("User", backref='user_orders')

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, user_id: {self.user_id}'
