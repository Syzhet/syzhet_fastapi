from datetime import datetime, timedelta
from typing import List

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import base_config
from ..db.base import get_session
from ..db.models.admin import Admin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


SECRET_KEY = base_config.admin.secret_key
ALGORITHM = base_config.admin.algoritm
TOKEN_EXPIRE = base_config.admin.token_expire
DELIMETR = base_config.admin.delimetr


def create_access_token(
    data: dict,
) -> str:
    """
    Creating an access token using
    SECRET_KEY and the encryption algorithm: ALGORITHM.
    """

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def check_access_token(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session)
) -> Admin:
    """Verifying the validity of the token."""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        userdata: List[str] = payload.get("sub")
    except JWTError:
        raise credentials_exception
    if not userdata:
        raise credentials_exception
    username: str = userdata.split(DELIMETR)[0]
    query = select(Admin).where(
        Admin.username == username,
    )
    obj = await session.execute(query)
    admin: Admin = obj.scalars().first()
    if not admin:
        raise credentials_exception
    return admin
