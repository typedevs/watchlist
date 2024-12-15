import pytest


@pytest.mark.anyio
@pytest.mark.dependency
async def test_create_movie(client):
    movie_data = {"name": "Jnception", "director_id": 1}
    response = await client.post(url="http://localhost:9001/movie", json=movie_data,
                                 follow_redirects=True)
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == 1
    assert data['name'] == 'Jnception'
