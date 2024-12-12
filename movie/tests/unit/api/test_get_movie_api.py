# import pytest
# from fastapi.testclient import TestClient
# from movie.src.main import app
# from movie.src.adapters.schemas.movie_schema import MovieResponse
# from movie.src.adapters.controllers.movie_controller import MovieController
#
#
# @pytest.mark.asyncio
# async def test_get_movie(unit_test_client, mock_movie_controller):
#     movie_id = 1
#     movie = {"id": movie_id, "name": "Movie 1", "director_id": 101}
#     mock_movie_controller.get_movie.return_value = movie
#
#     response = unit_test_client.get(f"/movie/{movie_id}")
#
#     assert response.status_code == 200
#     assert response.json() == movie
#     mock_movie_controller.get_movie.assert_called_once_with(movie_id)