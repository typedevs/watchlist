from movie.src.entities.movie_entity import MovieEntity


class MovieDictMapper:
    @staticmethod
    def dict_to_entity(document: dict) -> MovieEntity:
        return MovieEntity(
            id=document['id'],
            name=document['name'],
            director_id=document['director_id'],
        )
