from .base import async_session, init_models
import asyncio
from sqlalchemy import select
from .models.users import User


session = async_session()


async def test(session):
    print('session: ', session)
    result = await session.execute(select(User))
    print('result: ', result)
    res = result.scalars().all()
    print('res: ', res)


async def main():
    await init_models()
    await asyncio.sleep(5)
    print('init models ok')
    await asyncio.sleep(5)
    print('get session ok')
    await test(session)

asyncio.run(main())
