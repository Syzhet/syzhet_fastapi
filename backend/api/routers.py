from fastapi import APIRouter, Depends

from backend.db.base import get_session

from .user_router import user_router


router = APIRouter(
    dependencies=[Depends(get_session)]
)

router.include_router(user_router)
