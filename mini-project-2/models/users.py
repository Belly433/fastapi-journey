from beanie import Document, Link
from typing import Optional, List
from pydantic import EmailStr
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"