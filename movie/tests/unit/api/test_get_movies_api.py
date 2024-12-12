import pytest


@pytest.mark.asyncio
async def test_get_movies(unit_test_client, mock_movie_controller):
    movies = [
        {"id": 1, "name": "Movie 1", "director_id": 101},
        {"id": 2, "name": "Movie 2", "director_id": 102},
    ]
    mock_movie_controller.get_movies.return_value = movies

    response = unit_test_client.get("/movie")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Movie 1"
    assert data[0]["director_id"] == 101
    mock_movie_controller.get_movies.assert_called_once()
