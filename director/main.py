from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Director(BaseModel):
    id: int
    name: str


directors: list[Director] = []


@app.post("/")
async def create_director(director: Director):
    directors.append(director)
    return director


@app.delete("/{director_id}")
async def delete_director(director_id: int):
    for director in directors:
        if director.id == director_id:
            directors.remove(director)
            return {"message": "Director deleted"}
    return {"error": "Director not found"}
