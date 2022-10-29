from typing import List, Optional

from fastapi import APIRouter

from backend.db.schemas.users_schema import UserGet


user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@user_router.get('/', response_model=List[UserGet])
async def get_users(limit: Optional[str] = None):
    return []


@user_router.get('/{id}', response_model=UserGet)
async def get_user(id: int):
    return {'id': id}
