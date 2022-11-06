from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from ..db.schemas.token_schema import Token, TokenCreate
from ..db.base import get_session
from ..auth.auth import authenticate_admin
from ..auth.token import create_access_token


token_router = APIRouter(
    prefix='/token',
    tags=['Token']
)


@token_router.post('/', response_model=Token)
async def get_token(
    data: TokenCreate,
    session: AsyncSession = Depends(get_session)
):
    admin = await authenticate_admin(
        session=session,
        username=data.username,
        password=data.password
    )
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad usernmae or password'
        )
    access_token = create_access_token(
        data={"sub": [admin.username, admin.hashed_password]}
    )
    await session.commit()
    return {"access_token": access_token, "token_type": "bearer"}
