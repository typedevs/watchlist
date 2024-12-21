from fastapi import APIRouter

from movie.src.infrastructures.fastapi.api import movie_api

routers = APIRouter()
router_list = [movie_api.router, ]

for router in router_list:
    routers.include_router(router)
