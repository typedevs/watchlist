from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from movie.src.adapters.controllers.movie_controller import MovieController
from movie.src.adapters.schemas.movie_schema import MovieCreateRequest, MovieResponse
from movie.src.core.containers import AppContainer

router = APIRouter(
    prefix="/movie",
    tags=["Movie"],
)


@router.post("/", response_model=MovieResponse)
@inject
async def create_movie(
        movie: MovieCreateRequest,
        controller: MovieController = Depends(Provide[AppContainer.movie_controller]),
):
    return await controller.create_movie(movie)
