from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_scoped_session, \
    async_sessionmaker
from asyncio import current_task

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/movie"

async_engine: AsyncEngine = create_async_engine(DATABASE_URL, future=True, echo=True)


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
