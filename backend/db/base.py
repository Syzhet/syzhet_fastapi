from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.config import base_config

PG_USER: str = base_config.db.db_user
PG_PASS: str = base_config.db.db_password
PG_HOST: str = base_config.db.db_host
PG_PORT: str = base_config.db.db_port
DATABASE: str = base_config.db.database


DATABASE_URL: str = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DATABASE}"
)

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

async_session: AsyncSession = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def init_models() -> None:
    """
    Function for deleting old tables from the database
    and creating new ones.
    """

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    """Function for creating a database connection session."""

    async with async_session() as session:
        yield session
