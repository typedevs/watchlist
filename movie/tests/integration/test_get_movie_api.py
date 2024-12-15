# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
#
# from movie.src.core.dependency_injection import RelationalDBModule, injector
# from movie.src.infrastructures.database.postgres import
# AsyncPostgreSQLEngine, initialize_postgres_db, \
#     AsyncPostgreSQLScopedSession
# from movie.src.main import app
# from movie.src.infrastructures.database.sql_models.base import Base
#
#
# # Test Database Setup
# @pytest.fixture(scope="module")
# async def test_db():
#     # Initialize test database
#     from sqlalchemy.ext.asyncio import AsyncSession
#     from sqlalchemy.orm import sessionmaker
#
#     # Create the test database tables
#     await initialize_postgres_db(Base)
#
#     # Create a session
#     SessionLocal = async_sessionmaker(
#         AsyncPostgreSQLEngine,
#         expire_on_commit=False,
#         autoflush=False,
#         autocommit=False,
#         class_=AsyncSession,
#     ),
#
#     yield SessionLocal  # Provide the session to the test
#
#     # Clean up
#
# @pytest.fixture(scope="module")
# def test_injector():
#     """Creates a test-specific injector for testing purposes."""
#     from injector import Injector
#
#     # Test dependencies to avoid the real database
#     injector = Injector([
#         # Provide a test database session instead of a real one
#         RelationalDBModule()  # your original module that includes MovieController, etc.
#     ])
#
#     return injector
#
# @pytest.fixture(scope="module")
# def client(test_db, test_injector):
#     app.dependency_overrides[injector] = test_injector  # Override injector
#     # This will allow us to test the FastAPI app
#     client = TestClient(app)
#     return client
#
#
#
# @pytest.mark.asyncio
# async def test_create_movie(client, test_injector):
#     # Prepare test data
#     movie_data = {
#         "name": "Inception",
#         "director_id": 1,
#     }
#
#
#     # Perform the API request
#     response = client.post("/movie", json=movie_data)
#
#     # Assert the response status code is 200 (success)
#     assert response.status_code == 200
#
#     # Assert the response matches the expected structure
#     movie_response = response.json()
#     assert "id" in movie_response
#     assert movie_response["name"] == movie_data["name"]
#     assert movie_response["director_id"] == movie_data["director_id"]
