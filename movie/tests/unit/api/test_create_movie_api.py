# import pytest
#
#
# @pytest.mark.asyncio
# async def test_create_movie(unit_test_client, mock_movie_controller):
#     movie_data = {"name": "New Movie", "director_id": 103}
#     created_movie = {"id": 3, **movie_data}
#     mock_movie_controller.create_movie.return_value = created_movie
#
#     response = unit_test_client.post("/movie", json=movie_data)
#
#     assert response.status_code == 200
#     assert response.json() == created_movie
#     mock_movie_controller.create_movie.assert_called_once()
