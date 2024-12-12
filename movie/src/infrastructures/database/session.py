from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_scoped_session, \
    async_sessionmaker
from asyncio import current_task

from movie.src.core.config import settings


async_engine: AsyncEngine = create_async_engine(settings.full_database_url, future=True, echo=True)


async_session = async_scoped_session(
    async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession,
    ),
    scopefunc=current_task,
)
