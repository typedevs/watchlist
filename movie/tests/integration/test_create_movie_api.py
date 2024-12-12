import pytest


# @pytest.mark.asyncio
# async def test_create_movie(integration_test_client):
#     payload = {"name": "Inception", "director_id": 1}
#
#     response = integration_test_client.post("/", json=payload)
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Inception"
#     assert data["director_id"] == 1
