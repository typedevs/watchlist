from typing import Any, Optional, Type

from motor.motor_asyncio import AsyncIOMotorClient

from movie.src.adapters.repositories.document_db.movie_repository import DocumentDBMovieRepository
from movie.src.adapters.unit_of_works.base_unit_of_work import UnitOfWork


class DocumentDBUnitOfWork(UnitOfWork[DocumentDBMovieRepository]):
    def __init__(
        self,
        engine: AsyncIOMotorClient,
        document_repository: DocumentDBMovieRepository,
    ):
        super().__init__(document_repository)
        self._engine = engine

    async def __aenter__(self):
        self._session = await self._engine.start_session()
        self._session.start_transaction()
        self.repository.session = self._session

        return self

    async def __aexit__(
        self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], tb: Any
    ):
        try:
            if exc_type is None:
                await self._session.commit_transaction()
            else:
                await self._session.abort_transaction()
        finally:
            await self._session.end_session()
