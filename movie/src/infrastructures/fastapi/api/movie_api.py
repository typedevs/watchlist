from typing import List

from fastapi import APIRouter

from movie.src.adapters.controllers.movie_controller import MovieController
from movie.src.adapters.schemas.movie_schema import MovieCreateRequest, MovieResponse
from movie.src.core.dependency_injection import injector

router = APIRouter(
    prefix="/movie",
    tags=["Movie"],
)


@router.get("/", response_model=List[MovieResponse])
async def get_movies():
    controller = injector.get(MovieController)
    return await controller.get_movies()


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie(
    movie_id: int,
):
    controller = injector.get(MovieController)
    return await controller.get_movie(movie_id)


@router.post("/", response_model=MovieResponse)
async def create_movie(
    movie: MovieCreateRequest,
):
    controller = injector.get(MovieController)
    return await controller.create_movie(movie)


@router.delete("/{movie_id}")
async def delete_movie(
    movie_id: int,
):
    controller = injector.get(MovieController)
    return await controller.remove_movie(movie_id)
