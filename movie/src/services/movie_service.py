from typing import List

from movie.src.adapters.schemas.movie_schema import MovieCreateRequest
from movie.src.adapters.unit_of_works.base_unit_of_work import UnitOfWork
from movie.src.entities.movie_entity import MovieEntity
from movie.src.services.base_service import Service


class MovieService(Service[MovieEntity]):
    def __init__(self, movie_uow: UnitOfWork):
        self.movie_uow = movie_uow

    async def create(self, movie: MovieCreateRequest) -> MovieEntity:
        movie_entity = MovieEntity(name=movie.name, director_id=movie.director_id)
        async with self.movie_uow as uow:
            return await uow.repository.add(entity=movie_entity)

    async def get(self, entity_id: int) -> MovieEntity:
        async with self.movie_uow as uow:
            return await uow.repository.get(entity_id=entity_id)

    async def get_list(self) -> List[MovieEntity]:
        async with self.movie_uow as uow:
            return await uow.repository.get_multi()

    async def delete(self, entity_id: int):
        async with self.movie_uow as uow:
            await uow.repository.delete(entity_id=entity_id)
