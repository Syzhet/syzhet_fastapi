from datetime import datetime, timedelta
from typing import List

from jose import jwt, JWTError
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
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
):
    """
    Создание токена доступа с использованием,
    SECRET_KEY и алгоритма шифрования: ALGORITHM)
    """

    print('create_access_token: ', data)
    print('create_access_token: ', type(data))
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt


async def check_access_token(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session)
):
    print('start check_access_token------------')
    print('check_access_token - session: ', session)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print('payload: ', payload)
        userdata: List[str] = payload.get("sub")
        print('userdata: ', userdata)
    except JWTError:
        raise credentials_exception
    if not userdata:
        raise credentials_exception
    username = userdata.split(DELIMETR)[0]
    print(username)
    query = select(Admin).where(
        Admin.username == username,
    )
    obj = await session.execute(query)
    admin = obj.scalars().first()
    if not admin:
        raise credentials_exception
    return admin
