from motor.motor_asyncio import AsyncIOMotorClient

from movie.src.core.config import settings

AsyncMongoDBEngine = AsyncIOMotorClient(settings.full_mongo_database_url)


async def initialize_mongo_db():
    if settings.RESET_DB:
        await AsyncMongoDBEngine.drop_database(AsyncMongoDBEngine.get_default_database().name)

    db = AsyncMongoDBEngine[settings.DATABASE_NAME]
    collection = db[settings.COLLECTION_NAME]
    await collection.create_index([('id', 1)], unique=True)
