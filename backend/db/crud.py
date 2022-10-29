from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models.users import User
from .models.orders import Order


async def get_list(
    session: AsyncSession,
    model: Union[User, Order],
    limit: int = None
):
    result = await session.execute(
        select(model).order_by(model.updated_on.desc()).limit(limit)
    )
    return result.scalars().all()
