import asyncio
from  motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

uri = settings.DataBase_url
client = AsyncIOMotorClient(uri)

async def connect_to_mongo():
    try:
        # Ping the server to verify connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Connection failed: {e}")
if __name__ == "__main__":
    asyncio.run(connect_to_mongo())

    