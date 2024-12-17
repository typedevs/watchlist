from typing import List

from movie.src.adapters.schemas.movie_schema import MovieCreateRequest, MovieResponse
from movie.src.services.base_service import Service


class MovieController:

    def __init__(self, movie_service: Service):
        self.movie_service = movie_service

    async def create_movie(self, movie_request: MovieCreateRequest) -> MovieResponse:
        new_movie = await self.movie_service.create(movie_request)
        return MovieResponse.from_entity(new_movie)

    async def get_movie(self, movie_id: int) -> MovieResponse:
        movie = await self.movie_service.get(entity_id=movie_id)
        return MovieResponse.from_entity(movie)

    async def get_movies(self) -> List[MovieResponse]:
        movies = await self.movie_service.get_list()
        return [MovieResponse.from_entity(movie) for movie in movies]

    async def remove_movie(self, movie_id: int) -> dict:
        await self.movie_service.delete(entity_id=movie_id)
        return {"detail": "Movie deleted successfully"}
