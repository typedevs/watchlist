from pydantic import BaseModel

from movie.src.entities.movie_entity import MovieEntity


class MovieCreateRequest(BaseModel):
    name: str
    director_id: int


class MovieResponse(BaseModel):
    id: int
    name: str
    director_id: int

    @classmethod
    def from_entity(cls, movie: MovieEntity):
        return cls(id=movie.id, name=movie.name, director_id=movie.director_id)
