# import asyncio
# from httpx import AsyncClient
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from fastapi import FastAPI
# import pytest
# from sqlalchemy.orm import sessionmaker
#
# from movie.src.infrastructures.database.sql_models import MovieModel
# from movie.src.infrastructures.database.sql_models.base import Base
#
# async_engine = create_async_engine(
#     url='postgresql+asyncpg://...',
#     echo=True,
# )
#
#
# # drop all database every time when test complete
# @pytest.fixture(scope='session')
# async def async_db_engine():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#     yield async_engine
#
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#
#
# # truncate all table to isolate tests
# @pytest.fixture(scope='function')
# async def async_db(async_db_engine):
#     async_session = sessionmaker(
#         expire_on_commit=False,
#         autocommit=False,
#         autoflush=False,
#         bind=async_db_engine,
#         class_=AsyncSession,
#     )
#
#     async with async_session() as session:
#         await session.begin()
#
#         yield session
#
#         await session.rollback()
#
#         for table in reversed(Base.metadata.sorted_tables):
#             await session.execute(f'TRUNCATE {table.name} CASCADE;')
#             await session.commit()
#
#
# @pytest.fixture(scope='session')
# async def async_client() -> AsyncClient:
#     return AsyncClient(base_url='http://localhost')
#
#
# # let test session to know it is running inside event loop
# @pytest.fixture(scope='session')
# def event_loop():
#     policy = asyncio.get_event_loop_policy()
#     loop = policy.new_event_loop()
#     yield loop
#     loop.close()
#
#
# # assume we have a example model
# @pytest.fixture
# async def async_example_orm(async_db: AsyncSession) -> MovieModel:
#     example = MovieModel(name='test', director_id=18)
#     async_db.add(example)
#     await async_db.commit()
#     await async_db.refresh(example)
#     return example
