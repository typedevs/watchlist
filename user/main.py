from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str


users: list[User] = []


@app.post("/")
async def create_user(user: User):
    users.append(user)
    return user


@app.get("/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


@app.get("/{user_id}/watchlist")
async def get_user_watchlist(user_id: int):
    # Call watchlist microservice to get watchlist
    import requests

    response = requests.get(f"http://watchlist:8003/watchlist/{user_id}")
    if response.status_code == 200:
        return response.json()
    return {"error": "Watchlist not found"}
