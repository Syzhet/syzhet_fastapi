from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.models.admin import Admin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares the transmitted password and
    the hash password stored in the database.
    """

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Converts the user's password into a hash password
    for storage in the database.
    """

    return pwd_context.hash(password)


async def get_admin(session: AsyncSession, username: str) -> Admin:
    """Returns the administrator object from the database."""

    query = select(Admin).where(Admin.username == username)
    obj = await session.execute(query)
    admin: Admin = obj.scalars().first()
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad username or password'
        )
    return admin


async def authenticate_admin(
    session: AsyncSession,
    username: str,
    password: str
) -> Admin:
    """Authentication, verification of the username and password."""

    admin: Admin = await get_admin(session, username)
    if not verify_password(password, admin.hashed_password):
        return False
    return admin
