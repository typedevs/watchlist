from sqlalchemy.ext.asyncio import AsyncSession

from movie.src.adapters.repositories.movie_repository import MovieRepository
from movie.src.adapters.unit_of_works.base_unit_of_work import UnitOfWork


class MovieUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession, movie_repository: MovieRepository):
        super().__init__(movie_repository)
        self._session = session

    async def __aenter__(self):
        await self._session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()
            await self.remove()

    async def remove(self):
        from movie.src.infrastructures.database.session import async_session
        await async_session.remove()
