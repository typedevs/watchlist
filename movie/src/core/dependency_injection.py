from injector import Injector, Module, provider, singleton
from motor.motor_asyncio import AsyncIOMotorCollection
from sqlalchemy.ext.asyncio import AsyncSession


from .config import settings
from ..adapters.controllers.movie_controller import MovieController

from ..adapters.repositories.document_db.movie_repository import DocumentDBMovieRepository
from ..adapters.repositories.relational_db.movie_repository import RelationalDBMovieRepository
from ..adapters.unit_of_works.base_unit_of_work import UnitOfWork
from ..adapters.unit_of_works.document_db_unit_of_work import DocumentDBUnitOfWork
from ..adapters.unit_of_works.relational_db_unit_of_work import RelationalDBUnitOfWork
from ..infrastructures.database import IS_RELATIONAL_DB, IS_DOCUMENT_DB
from ..infrastructures.database.mongodb import AsyncMongoDBEngine
from ..services.base_service import Service
from ..services.movie_service import MovieService


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
        self, session: AsyncSession, movie_repository: RelationalDBMovieRepository
    ) -> UnitOfWork:
        return RelationalDBUnitOfWork(session, movie_repository)

    @provider
    def provide_movie_service(self, unit_of_work: UnitOfWork) -> Service:
        return MovieService(unit_of_work)

    @provider
    def provide_movie_controller(self, movie_service: Service) -> MovieController:
        return MovieController(movie_service)


class DocumentDBModule(Module):
    @singleton
    @provider
    def provide_async_mongo_collection(
        self,
    ) -> AsyncIOMotorCollection:
        return AsyncMongoDBEngine[settings.DATABASE_NAME][settings.COLLECTION_NAME]

    @provider
    def provide_movie_repository(
        self,
        collection: AsyncIOMotorCollection,
    ) -> DocumentDBMovieRepository:
        return DocumentDBMovieRepository(collection, session=None)

    @provider
    def provide_async_motor_unit_of_work(
        self, movie_repository: DocumentDBMovieRepository
    ) -> UnitOfWork:
        from movie.src.infrastructures.database.mongodb import AsyncMongoDBEngine

        return DocumentDBUnitOfWork(AsyncMongoDBEngine, movie_repository)


class DatabaseModuleFactory:
    def create_module(self):
        if IS_RELATIONAL_DB:
            return RelationalDBModule()
        elif IS_DOCUMENT_DB:
            return DocumentDBModule()

        raise RuntimeError(
            'Invalid database type configuration. It\'s neither relational nor NoSQL'
        )


injector = Injector([DatabaseModuleFactory().create_module()])
