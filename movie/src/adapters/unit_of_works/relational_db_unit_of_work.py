from typing import Any, Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession

from movie.src.adapters.repositories.relational_db.movie_repository import \
    RelationalDBMovieRepository
from movie.src.adapters.unit_of_works.base_unit_of_work import UnitOfWork


class RelationalDBUnitOfWork(UnitOfWork[RelationalDBMovieRepository]):

    def __init__(self, session: AsyncSession, relational_repository: RelationalDBMovieRepository):
        super().__init__(relational_repository)
        self._session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: Optional[Type[BaseException]],
                        exc: Optional[BaseException], tb: Any):
        try:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
        finally:
            await self._session.close()
            await self.remove()

    async def remove(self):
        from movie.src.infrastructures.database import AsyncScopedSession

        await AsyncScopedSession.remove()
