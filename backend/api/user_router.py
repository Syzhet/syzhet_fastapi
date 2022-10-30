from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.db.base import get_session
from backend.db.schemas.users_schema import UserCreate, UserGet
from backend.db.crud import get_list, get_obj, create_obj
from backend.db.models.users import User


user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get('/', response_model=List[UserGet])
async def get_users(
    session: AsyncSession = Depends(get_session),
    limit: Optional[str] = None
):
    users = await get_list(session=session, model=User, limit=limit)
    return users


@user_router.get('/{id}', response_model=UserGet)
async def get_user(id: int, session: AsyncSession = Depends(get_session)):
    user = await get_obj(session=session, id=id, model=User)
    return user


@user_router.post(
    '/',
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):

    await create_obj(
        session=session,
        data=data,
        model=User
    )
    return Response(status_code=status.HTTP_201_CREATED)


@user_router.put(
    '/{id}',
    status_code=status.HTTP_201_CREATED
)
async def update_user(
    id: int,
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    # user = await get_obj(session=session, id=id, model=User)
    user = select(User).update()
    result = await session.execute(user)
    res = result.scalars().first()
    print('-----------------------------------------user', res)
    for field, value in data:
        setattr(res, field, value)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', res)
    await session.commit()
    return res
