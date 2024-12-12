# from httpx import AsyncClient
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# import pytest
#
# from movie.src.infrastructures.database.sql_models import MovieModel
#
# pytestmark = pytest.mark.asyncio
#
#
# async def test_get_movie(async_client: AsyncClient, async_db: AsyncSession,
#                            async_example_orm) -> None:
#     response = await async_client.get(f'/movie/{async_example_orm.id}')
#
#     assert response.status_code == 200
#     assert (await async_db.execute(select(MovieModel).filter_by(id=async_example_orm.id)
#                                    )).scalar_one().id == async_example_orm.id
