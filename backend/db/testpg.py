from .base import async_session, init_models
import asyncio
from sqlalchemy import select
from .models.users import User
from .models.admin import Admin
from ..auth.auth import get_password_hash


session = async_session()


async def test(session):
    print('session: ', session)
    result = await session.execute(select(User))
    print('result: ', result)
    res = result.scalars().all()
    print('res: ', res)


async def create_admin(session):
    hashed_password = get_password_hash('secret')
    admin = Admin(username='khasguz', hashed_password=hashed_password)
    session.add(admin)
    await session.commit()


async def main():
    await init_models()
    await asyncio.sleep(5)
    print('init models ok')
    await asyncio.sleep(5)
    print('get session ok')
    await test(session)
    await create_admin(session)
    print('create admin ok')


asyncio.run(main())
