import asyncio

import pytest
from sqlalchemy import text
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from movie.src.core.config import settings
from movie.src.infrastructures.database.sql_models.base import Base


@pytest.fixture(scope="session")
def event_loop():
    """Create an event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_database_url(event_loop):
    """Create a separate admin engine to manage the test database."""
    # Parse the main database URL
    original_url = make_url(settings.full_database_url)
    test_db_name = "test_" + original_url.database

    # Create an admin engine connected to the system database
    admin_url = original_url.set(database="postgres")  # Connect to the system DB
    admin_engine = create_async_engine(str(admin_url), future=True, echo=True)

    async with admin_engine.connect() as connection:
        # Drop the test database if it exists
        await connection.execute(text(f"DROP DATABASE IF EXISTS {test_db_name}"))
        # Create a new test database
        await connection.execute(text(f"CREATE DATABASE {test_db_name}"))

    # Dispose of the admin engine
    await admin_engine.dispose()

    # Return the test database URL
    test_url = str(original_url.set(database=test_db_name))
    yield test_url

    # Cleanup: Drop the test database after tests finish
    admin_engine = create_async_engine(str(admin_url), future=True, echo=True)
    async with admin_engine.connect() as connection:
        await connection.execute(text(f"DROP DATABASE IF EXISTS {test_db_name}"))
    await admin_engine.dispose()


@pytest.fixture(scope="session")
async def postgres_db(test_database_url):
    """Set up the test database and provide an async engine."""
    async_engine = create_async_engine(test_database_url, future=True, echo=True, isolation_level="SERIALIZABLE")
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield async_engine
    await async_engine.dispose()


@pytest.fixture
def postgres_session_factory(postgres_db):
    yield async_sessionmaker(
        postgres_db,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession,
    )


@pytest.fixture
def postgres_session(postgres_session_factory):
    return postgres_session_factory()
