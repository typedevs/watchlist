from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Watchlist(BaseModel):
    id: int
    user_id: int
    movie_id: int


watchlists: list[Watchlist] = []


@app.post("/watchlist/")
async def create_watchlist(watchlist: Watchlist):
    watchlists.append(watchlist)
    return watchlist


@app.delete("/watchlist/{watchlist_id}")
async def delete_watchlist(watchlist_id: int):
    for watchlist in watchlists:
        if watchlist.id == watchlist_id:
            watchlists.remove(watchlist)
            return {"message": "Watchlist deleted"}
    return {"error": "Watchlist not found"}


@app.get("/watchlist/{user_id}")
async def get_watchlist(user_id: int):
    watchlist_movies: list[dict[str, str]] = []
    for watchlist in watchlists:
        if watchlist.user_id == user_id:
            # Call movie microservice to get movie details
            import requests

            response = requests.get(
                f"http://movie:8001/movie/{watchlist.movie_id}"
            )
            if response.status_code == 200:
                movie = response.json()
                # Call director microservice to get director details
                response = requests.get(
                    f"http://director:8002/director/{movie['director_id']}"
                )
                if response.status_code == 200:
                    director = response.json()
                    watchlist_movies.append(
                        {
                            "movie_name": movie["name"],
                            "director_name": director["name"],
                        }
                    )
    return watchlist_movies
