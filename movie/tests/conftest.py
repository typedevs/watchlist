# flake8: noqa

import os
from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient
from pytest import Config

from movie.src.infrastructures.database import IS_RELATIONAL_DB, initialize_db
from movie.src.infrastructures.database.postgres import AsyncPostgreSQLEngine, \
    AsyncPostgreSQLScopedSession


def pytest_configure(config: Config):
    echo = print  # ignore: remove-print-statements
    echo(__file__)
    echo(f'DATABASE_URL={os.environ["DATABASE_URL"]}')


@pytest.fixture(scope='session')
def anyio_backend():
    yield 'asyncio'


@pytest.fixture(scope='session')
async def client():
    async with AsyncClient() as ac:
        yield ac


@pytest.fixture(scope='session')
async def mock_controller():
    movie_repository = AsyncMock()
    movie_uow = AsyncMock()
    movie_uow.__aenter__.return_value = movie_uow
    movie_uow.repository = movie_repository
    movie_service = AsyncMock()
    movie_service.movie_uow = movie_uow
    controller = AsyncMock()
    controller.movie_service = movie_service

    yield controller


if IS_RELATIONAL_DB:
    from sqlalchemy import event
    from sqlalchemy.sql import text

    from movie.src.infrastructures.database.sql_models.base import Base

    TEST_DB_NAME = "arian_test"

    @pytest.fixture(scope='package', autouse=True)
    async def engine():
        await initialize_db(declarative_base=Base)

    @pytest.fixture(scope='function', autouse=True)
    async def session():
        async with AsyncPostgreSQLEngine.connect() as conn:
            await conn.execute(text('BEGIN'))
            await conn.begin_nested()

            async_session = AsyncPostgreSQLScopedSession(bind=conn)

            @event.listens_for(async_session.sync_session, 'after_transaction_end')
            def end_savepoint(*args, **kwargs):
                if conn.closed:
                    return
                if not conn.in_nested_transaction():
                    conn.sync_connection.begin_nested()

            yield async_session

            await AsyncPostgreSQLScopedSession.remove()

    @pytest.fixture(scope='function', autouse=True)
    def patch_functions(session):
        with (patch('movie.src.infrastructures.database.postgres.get_async_postgresql_session',
                    return_value=session),
              patch(
                  'movie.src.adapters.unit_of_works.relational_db_unit_of_work.RelationalDBUnitOfWork.remove',
                  new_callable=AsyncMock),
              ):
            yield
