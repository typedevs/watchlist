from asyncio import current_task
from typing import AsyncGenerator, Type

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_scoped_session, \
    async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from movie.src.core.config import settings

AsyncPostgreSQLEngine: AsyncEngine = create_async_engine(settings.DATABASE_URL, future=True,
                                                         echo=True)

AsyncPostgreSQLScopedSession = async_scoped_session(
    async_sessionmaker(
        AsyncPostgreSQLEngine,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession,
    ),
    scopefunc=current_task,
)


async def initialize_postgres_db(declarative_base: Type[DeclarativeBase]):
    async_engine = AsyncPostgreSQLEngine
    metadata = declarative_base.metadata

    async with async_engine.begin() as connection:

        await connection.run_sync(metadata.create_all)

    await async_engine.dispose()


def get_async_postgresql_session() -> AsyncSession:
    return AsyncPostgreSQLScopedSession()


async def async_postgresql_session_context_manager() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncPostgreSQLScopedSession() as session:
        yield session
