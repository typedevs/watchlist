import pytest
import requests


@pytest.mark.usefixtures("postgres_db")
def test_create_movie_api():
    url = "http://127.0.0.1:8002"
    r = requests.post(f"{url}/movie", json={"name": "interstellar", "director_id": 12})
    assert r.status_code == 200
    assert r.json().get("name") == "interstellar"
