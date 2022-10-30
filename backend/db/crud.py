from typing import Union

from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from .models.users import User
from .models.orders import Order
from .schemas.users_schema import UserCreate


async def get_list(
    session: AsyncSession,
    model: Union[User, Order],
    limit: int = None
):
    query = select(model).order_by(model.updated_on.desc())
    if limit:
        query = query.limit(limit)
    result = await session.execute(query)
    await session.commit()
    return result.scalars().all()


async def get_obj(
    session: AsyncSession,
    model: Union[User, Order],
    id: int
):
    object = await session.get(model, id)
    if not object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'bad id': id}
        )
    return object


async def create_obj(
    session: AsyncSession,
    model: Union[User, Order],
    data: UserCreate
):
    object = model(**data.dict())
    session.add(object)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This user is already exists'
        )
    return object
