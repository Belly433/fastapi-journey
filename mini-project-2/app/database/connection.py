import os
from dotenv import load_dotenv
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.events import Event
from models.users import User

load_dotenv()
class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)

        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User]
        )