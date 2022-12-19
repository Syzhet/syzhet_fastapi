from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..base import Base


class Order(Base):
    """Сlass for representing a order in database."""

    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String())
    user_id = Column(
        Integer(),
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    updated_on = Column(DateTime(), server_default=func.now())
    user = relationship(
        "User",
        back_populates='orders',
        cascade='save-update, merge, delete',
        passive_deletes=True,
        lazy='joined')

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, user_id: {self.user_id}'
