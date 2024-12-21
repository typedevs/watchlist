from dataclasses import dataclass


@dataclass
class MovieEntity:
    id: int = None
    name: str = None
    director_id: int = None
