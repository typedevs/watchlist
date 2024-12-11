from dependency_injector.wiring import inject

from movie.src.adapters.schemas.movie_schema import MovieCreateRequest, MovieResponse
from movie.src.services.movie_service import MovieService


class MovieController:
    @inject
    def __init__(self, movie_service: MovieService):
        self.movie_service = movie_service

    async def create_movie(self, movie_request: MovieCreateRequest) -> MovieResponse:
        new_movie = await self.movie_service.create(
            movie_request
        )
        return MovieResponse.from_entity(new_movie)
