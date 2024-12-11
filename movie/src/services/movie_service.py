from dependency_injector.wiring import inject

from movie.src.adapters.schemas.movie_schema import MovieCreateRequest
from movie.src.adapters.unit_of_works.movie_unit_of_work import MovieUnitOfWork
from movie.src.entities.movie_entity import MovieEntity
from movie.src.services.base_service import Service


class MovieService(Service[MovieEntity]):
    @inject
    def __init__(self, movie_uow: MovieUnitOfWork):
        self.movie_uow = movie_uow

    async def create(self, movie: MovieCreateRequest) -> MovieEntity:
        movie_entity = MovieEntity(name=movie.name, director_id=movie.director_id)
        async with self.movie_uow as uow:
            await uow.repository.add(entity=movie_entity)
        return movie_entity

    async def get(self, movie_id: int) -> MovieEntity:
        async with self.movie_uow as uow:
            return await uow.repository.get(entity_id=movie_id)

    async def get_list(self):
        async with self.movie_uow as uow:
            return await uow.repository.list()

    async def delete(self, movie_id: int):
        async with self.movie_uow as uow:
            await uow.repository.delete(entity_id=movie_id)
