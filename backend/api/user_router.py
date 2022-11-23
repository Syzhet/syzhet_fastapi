from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.base import get_session
from backend.db.crud import (count_obj, create_obj, delete_obj, get_obj,
                             get_user_list, update_obj)
from backend.db.models.users import User
from backend.db.schemas.users_schema import UserCreate, UserGet, UserWithOrder

from ..auth.token import check_access_token

user_router: APIRouter = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[Depends(check_access_token)]
)


@user_router.get('/', response_model=List[UserWithOrder])
async def get_users(
    session: AsyncSession = Depends(get_session),
    limit: Optional[str] = None,
    tgid: Optional[int] = None
):
    """Handler for the GET path request 'domen/api/v1/users/'."""

    users = await get_user_list(
        session=session, model=User,
        limit=limit,
        tgid=tgid
    )
    return users


@user_router.get('/count')
async def users_count(session: AsyncSession = Depends(get_session)):
    """Handler for the GET path request 'domen/api/v1/users/count/'."""

    count: int = await count_obj(session=session, model=User)
    return {'count_users': f'count users: {count}'}


@user_router.get('/{id}', response_model=UserWithOrder)
async def get_user(id: int, session: AsyncSession = Depends(get_session)):
    """Handler for the GET path request 'domen/api/v1/users/{id}'."""

    user: User = await get_obj(session=session, id=id, model=User)
    return user


@user_router.post(
    '/',
    response_model=UserGet,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    """Handler for the POST path request 'domen/api/v1/users/'."""

    user: User = await create_obj(
        session=session,
        data=data,
        model=User
    )
    return user


@user_router.put(
    '/{id}',
    response_model=UserGet,
    status_code=status.HTTP_201_CREATED
)
async def update_user(
    id: int,
    data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    """Handler for the PUT path request 'domen/api/v1/users/{id}/'."""

    return await update_obj(
        session=session,
        model=User,
        data=data,
        id=id
    )


@user_router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
    id: int,
    session: AsyncSession = Depends(get_session)
):
    """Handler for the DELETE path request 'domen/api/v1/users/{id}/'."""

    await delete_obj(
        session=session,
        model=User,
        id=id
    )
    return Response(content='Объект удален')
