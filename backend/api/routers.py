from fastapi import APIRouter

from .user_router import user_router


router = APIRouter()

router.include_router(user_router)
