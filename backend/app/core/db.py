from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from app.core.errors import AppException

class Database:
    client: AsyncIOMotorClient = None
    
    @classmethod
    async def connect_db(cls):
        try:
            cls.client = AsyncIOMotorClient(settings.mongodb_url, serverSelectionTimeoutMS=5000)
            await cls.client.admin.command('ping')  # Test the connection
            print("Connected to MongoDB!")
        except Exception as e:
            raise AppException(
                message="Failed to connect to MongoDB",
                status_code=500,
                details={"error": str(e)}
            )
    
    @classmethod
    async def close_db(cls):
        if cls.client is not None:
            cls.client.close()
            print("Closed MongoDB connection.")
    
    @classmethod
    def get_db(cls):
        if cls.client is None:
            raise AppException(
                message="Database connection not initialized",
                status_code=500
            )
        return cls.client[settings.database_name]

db = Database()
