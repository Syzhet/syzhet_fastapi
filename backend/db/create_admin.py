import asyncio
import logging

from sqlalchemy.exc import IntegrityError

from ..auth.auth import get_password_hash
from ..config import base_config
from .base import async_session
from .models.admin import Admin

logging.basicConfig(
    level=logging.INFO,
    format=(
        u'%(filename)s:%(lineno)d: '
        u'#%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
)

ADMIN_LOGIN = base_config.admin.login
ADMIN_PASSWORD = base_config.admin.password


async def create_admin():
    hashed_password = get_password_hash(ADMIN_PASSWORD)
    admin = Admin(username=ADMIN_LOGIN, hashed_password=hashed_password)
    async with async_session() as session:
        async with session.begin():
            session.add(admin)
            try:
                await session.commit()
            except IntegrityError:
                logging.info('Admin already existts')


async def main():
    await create_admin()
    print('create admin ok')


if __name__ == '__main__':
    asyncio.run(main())
