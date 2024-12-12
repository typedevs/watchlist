from dependency_injector import containers, providers

from movie.src.adapters.repositories.movie_repository import MovieRepository
from movie.src.adapters.unit_of_works.movie_unit_of_work import MovieUnitOfWork
from movie.src.infrastructures.database.session import async_session
from movie.src.adapters.controllers.movie_controller import MovieController
from movie.src.services.movie_service import MovieService


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["movie.src.infrastructures.fastapi.api.movie_api"])

    db_session_factory = providers.Singleton(async_session)
    movie_repository = providers.Factory(
        MovieRepository,
        session=db_session_factory
    )
    movie_uow = providers.Factory(
        MovieUnitOfWork,
        session=db_session_factory,
        movie_repository=movie_repository
    )
    movie_service = providers.Factory(MovieService, movie_uow=movie_uow)
    movie_controller = providers.Factory(MovieController, movie_service=movie_service)
