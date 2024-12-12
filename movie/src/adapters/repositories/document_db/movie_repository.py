from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection

from movie.src.core.exceptions import MovieNotFoundException
from movie.src.entities.movie_entity import MovieEntity
from ..base_repository import Repository
from .mapper import MovieDictMapper


class DocumentDBMovieRepository(Repository):

    def __init__(
            self,
            collection: AsyncIOMotorCollection,
            session: Optional[AsyncIOMotorClientSession] = None,
    ):
        self.collection = collection
        self.session = session

    async def get(self, entity_id: int) -> MovieEntity:
        try:
            document = await self.collection.find_one()
            if not document:
                raise MovieNotFoundException
        except StopAsyncIteration:
            raise MovieNotFoundException

        return MovieDictMapper.dict_to_entity(document)

    async def add(self, entity: MovieEntity) -> None:
        document = {}
        await self.collection.insert_one(document, session=self.session)

    async def get_multi(self):
        pass

    async def delete(self, entity_id: int):
        pass


