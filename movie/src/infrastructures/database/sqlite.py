from asyncio import current_task
from typing import AsyncGenerator, Type

from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, async_sessionmaker, \
    create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text

from movie.src.core.config import settings

AsyncSQLiteEngine = create_async_engine(
    settings.DATABASE_URL,
)

AsyncSQLiteScopedSession = async_scoped_session(
    async_sessionmaker(
        AsyncSQLiteEngine,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession,
    ),
    scopefunc=current_task,
)


@event.listens_for(AsyncSQLiteEngine.sync_engine, 'connect')
def connect(dbapi_conn, connection_record):
    dbapi_conn.execute('PRAGMA foreign_keys = ON;')


async def initialize_sqlite_db(
    declarative_base: Type[DeclarativeBase],
):
    async_engine = AsyncSQLiteEngine
    metadata = declarative_base.metadata

    async with async_engine.begin() as connection:
        await connection.execute(text('PRAGMA foreign_keys = ON;'))

        if settings.RESET_TEST_DB:
            await connection.run_sync(metadata.drop_all)

        await connection.run_sync(metadata.create_all)

    if (f'{async_engine.url.get_backend_name()}:///{async_engine.url.database}'
            != 'sqlite:///:memory:'):
        await async_engine.dispose()


def get_async_sqlite_session() -> AsyncSession:
    return AsyncSQLiteScopedSession()


async def async_sqlite_session_context_manager() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSQLiteScopedSession() as session:
        yield session
