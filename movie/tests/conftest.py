from asyncio import current_task

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session

from movie.src.adapters.controllers.movie_controller import MovieController
from movie.src.core.containers import AppContainer
from movie.src.infrastructures.database.models.base import Base
from movie.src.main import app


@pytest.fixture
def mock_movie_controller(mocker):
    """Mock the MovieController for dependency injection."""
    return mocker.Mock(spec=MovieController)


@pytest.fixture
def unit_test_client(mock_movie_controller):
    """Set up the test client with a mocked container."""
    container = AppContainer()
    container.movie_controller.override(mock_movie_controller)

    app.container = container
    with TestClient(app) as unit_test_client:
        yield unit_test_client


@pytest.fixture(scope="function")
def test_database_url():
    """Provide the database URL for the test database."""
    return "postgresql+asyncpg://postgres:postgres@localhost:5432/test_db"


@pytest.fixture(scope="function")
def test_engine(test_database_url):
    """Create the test engine for database connections."""
    return create_async_engine(test_database_url, future=True, echo=False)


@pytest.fixture(scope="function")
async def setup_test_database(test_engine):
    """Create and drop the database schema for tests."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def test_session_factory(test_engine):
    """Create a session factory for tests."""
    async_session = async_scoped_session(
        async_sessionmaker(
            bind=test_engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
            class_=AsyncSession,
        ),
        scopefunc=current_task,
    )
    return async_session


@pytest.fixture
def integration_test_client(test_session_factory):
    container = AppContainer()
    container.db_session_factory.override(test_session_factory)

    app.container = container
    with TestClient(app) as integration_test_client:
        yield integration_test_client
