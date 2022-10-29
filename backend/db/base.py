from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


from backend.config import base_config


PG_USER = base_config.db.db_user
PG_PASS = base_config.db.db_password
PG_HOST = base_config.db.db_host
PG_PORT = base_config.db.db_port
DATABASE = base_config.db.database


DATABASE_URL = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DATABASE}"
)

# DATABASE_URL = (
#     "postgresql+asyncpg://test:test@localhost:5432/syzhet"
# )


engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session


import asyncio

if __name__ == '__main__':
    asyncio.run(init_models())