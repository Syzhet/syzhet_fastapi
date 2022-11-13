from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.base import get_session
from backend.db.crud import (create_obj, delete_obj, get_obj, get_order_list,
                             update_obj)
from backend.db.models.orders import Order
from backend.db.schemas.orders_schema import OrderCreate, OrderGet, OrderUpdate

from ..auth.token import check_access_token

order_router = APIRouter(
    prefix='/orders',
    tags=['Orders'],
    dependencies=[Depends(check_access_token)]
)


@order_router.get('/', response_model=List[OrderGet])
async def get_orders(
    session: AsyncSession = Depends(get_session),
    limit: Optional[str] = None
):
    orders = await get_order_list(session=session, model=Order, limit=limit)
    return orders


@order_router.get('/{id}', response_model=OrderGet)
async def get_order(id: int, session: AsyncSession = Depends(get_session)):
    order = await get_obj(session=session, id=id, model=Order)
    return order


@order_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
async def create_order(
    data: OrderCreate,
    session: AsyncSession = Depends(get_session)
):

    order = await create_obj(
        session=session,
        data=data,
        model=Order
    )
    return order


@order_router.put(
    '/{id}',
    response_model=OrderGet,
    status_code=status.HTTP_201_CREATED
)
async def update_order(
    id: int,
    data: OrderUpdate,
    session: AsyncSession = Depends(get_session)
):
    return await update_obj(
        session=session,
        model=Order,
        data=data,
        id=id
    )


@order_router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_order(
    id: int,
    session: AsyncSession = Depends(get_session)
):
    await delete_obj(
        session=session,
        model=Order,
        id=id
    )
    return Response(content='Объект удален', media_type="text/plain")