from sqlalchemy import Column, Integer, String

from movie.src.infrastructures.database.sql_models.base import Base


class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    director_id = Column(Integer, nullable=False)
