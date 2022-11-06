from fastapi import APIRouter

from .user_router import user_router
from .order_router import order_router
from .token_router import token_router


router = APIRouter()

router.include_router(user_router)
router.include_router(order_router)
router.include_router(token_router)
