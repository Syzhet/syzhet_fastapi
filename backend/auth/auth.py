from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from passlib.context import CryptContext


from ..db.models.admin import Admin


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """Сравнивает переданный пароль и хеш-пароль хранящийся в базе."""

    print('verify_password: ', plain_password, ' + ', hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Преобразует пароль пользователя в хеш-пароль для хранения в базе."""

    print('get_password_hash: ', password)
    print('get_password_hash: ', pwd_context.hash(password))
    return pwd_context.hash(password)


async def get_admin(session: AsyncSession, username: str):
    """Функция возвращает объект юзера из базы."""

    print('get_user: ', session, ' + ', username)
    query = select(Admin).where(Admin.username == username)
    obj = await session.execute(query)
    admin = obj.scalars().first()
    print('get user: ', admin)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad usernmae or password'
        )
    return admin


async def authenticate_admin(
    session: AsyncSession,
    username: str,
    password: str
):
    """Аутентификация проверка юзернейма и пароля."""

    print('authenticate_user: ', session, ' + ', username, ' + ', password)
    admin = await get_admin(session, username)
    print('!!!!!!!!!!!!admin: ', admin)
    if not verify_password(password, admin.hashed_password):
        return False
    return admin
