from injector import Injector, Module, provider
from sqlalchemy.ext.asyncio import AsyncSession

from movie.src.adapters.controllers.movie_controller import MovieController
from movie.src.adapters.repositories.relational_db.movie_repository import \
    RelationalDBMovieRepository
from movie.src.adapters.unit_of_works.base_unit_of_work import UnitOfWork
from movie.src.adapters.unit_of_works.relational_db_unit_of_work import RelationalDBUnitOfWork
from movie.src.infrastructures.database import IS_RELATIONAL_DB
from movie.src.services.base_service import Service
from movie.src.services.movie_service import MovieService


class RelationalDBModule(Module):

    @provider
    def provide_async_session(self) -> AsyncSession:
        from movie.src.infrastructures.database import get_async_session

        return get_async_session()

    @provider
    def provide_movie_repository(self, session: AsyncSession) -> RelationalDBMovieRepository:
        return RelationalDBMovieRepository(session)

    @provider
    def provide_async_sqlalchemy_unit_of_work(
            self, session: AsyncSession,
            movie_repository: RelationalDBMovieRepository) -> UnitOfWork:
        return RelationalDBUnitOfWork(session, movie_repository)

    @provider
    def provide_movie_service(self, unit_of_work: UnitOfWork) -> Service:
        return MovieService(unit_of_work)

    @provider
    def provide_movie_controller(self, movie_service: Service) -> MovieController:
        return MovieController(movie_service)


class DatabaseModuleFactory:

    def create_module(self):
        if IS_RELATIONAL_DB:
            return RelationalDBModule()

        raise RuntimeError(
            'Invalid database type configuration. It\'s neither relational nor NoSQL')


injector = Injector([DatabaseModuleFactory().create_module()])
