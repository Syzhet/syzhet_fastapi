from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.base import get_session
from backend.db.schemas.users_schema import UserGet
from backend.db.crud import get_list
from backend.db.models.users import User


user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get('/', response_model=List[UserGet])
async def get_users(session: AsyncSession = Depends(get_session), limit: Optional[str] = None):
    users = await get_list(session=session, model=User, limit=limit)
    print(users)
    return []


@user_router.get('/{id}', response_model=UserGet)
async def get_user(id: int):
    return {'id': id}
