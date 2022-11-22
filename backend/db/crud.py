from typing import Union

from fastapi import HTTPException, status
from sqlalchemy import delete, select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .models.orders import Order
from .models.users import User
from .schemas.orders_schema import OrderCreate
from .schemas.users_schema import UserCreate


async def get_user_list(
    session: AsyncSession,
    model: User,
    limit: int = None,
    tgid: int = None
):
    query = select(model).options(selectinload(model.orders))
    if limit:
        query = query.limit(limit)
    if tgid:
        query = query.where(model.telegram_id == tgid)
    result = await session.execute(query.order_by(model.updated_on.desc()))
    await session.commit()
    return result.scalars().all()


async def get_order_list(
    session: AsyncSession,
    model: Order,
    limit: int = None
):
    query = select(model).options(selectinload(model.user))
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
    await session.commit()
    return object


async def create_obj(
    session: AsyncSession,
    model: Union[User, Order],
    data: Union[UserCreate, OrderCreate]
):
    object = model(**data.dict())
    session.add(object)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Error in data or this object is already exists'
        )
    return object


async def update_obj(
    session: AsyncSession,
    model: Union[User, Order],
    data: UserCreate,
    id: int
):
    obj = await get_obj(session=session, id=id, model=model)
    for field, value in data:
        setattr(obj, field, value)
    await session.commit()
    return obj


async def delete_obj(
    session: AsyncSession,
    model: Union[User, Order],
    id: int
):
    await session.execute(delete(model).where(model.id == id))
    await session.commit()


async def count_obj(
    session: AsyncSession,
    model: Union[User, Order]
):
    result = await session.execute(
        select([func.count()]).select_from(User).scalar()
    )
    return result
