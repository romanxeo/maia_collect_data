import databases
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from models import Base
from settings import settings

database = databases.Database(settings.DB_URL)


def get_db() -> databases.Database:
    return database


async def prepare_db():
    engine = create_async_engine(settings.DB_URL, poolclass=NullPool)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
