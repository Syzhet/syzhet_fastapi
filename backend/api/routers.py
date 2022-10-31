from fastapi import APIRouter

from .user_router import user_router
from .order_router import order_router


router = APIRouter()

router.include_router(user_router)
router.include_router(order_router)
