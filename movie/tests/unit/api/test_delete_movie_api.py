import pytest


@pytest.mark.asyncio
async def test_delete_movie(unit_test_client, mock_movie_controller):
    movie_id = 1
    mock_movie_controller.remove_movie.return_value = None

    response = unit_test_client.delete(f"/movie/{movie_id}")

    assert response.status_code == 200
    mock_movie_controller.remove_movie.assert_called_once_with(movie_id)
