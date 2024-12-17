from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from movie.src.adapters.repositories.base_repository import Repository
from movie.src.core.exceptions import MovieNotFoundException
from movie.src.entities.movie_entity import MovieEntity
from movie.src.infrastructures.database.sql_models.movie_model import MovieModel


class RelationalDBMovieRepository(Repository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, entity: MovieEntity) -> MovieEntity:
        json_entity = jsonable_encoder(entity)
        db_obj = MovieModel(**json_entity)
        self.session.add(db_obj)
        await self.session.flush()
        entity.id = db_obj.id
        return entity

    async def get(self, entity_id: int) -> Optional[MovieEntity]:
        result = await self.session.execute(select(MovieModel).filter_by(id=entity_id))
        db_movie = result.scalar_one_or_none()
        if db_movie:
            return MovieEntity(id=db_movie.id, name=db_movie.name,
                               director_id=db_movie.director_id)
        return None

    async def get_multi(self) -> List[MovieEntity]:
        result = await self.session.execute(select(MovieModel))
        db_movies = result.scalars().all()
        return [
            MovieEntity(id=movie.id, name=movie.name, director_id=movie.director_id)
            for movie in db_movies
        ]

    async def delete(self, entity_id: int) -> None:
        result = await self.session.execute(select(MovieModel).filter_by(id=entity_id))
        db_movie = result.scalar_one_or_none()
        if db_movie:
            await self.session.delete(db_movie)
        else:
            raise MovieNotFoundException
