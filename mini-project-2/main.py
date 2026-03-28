from fastapi import FastAPI
from database.connection import Settings
from routes.events import router as events_router
from routes.users import router as users_router

app = FastAPI()


@app.on_event("startup")
async def init_db():
    settings = Settings()
    await settings.initialize_database()


app.include_router(events_router, prefix="/events", tags=["events"])
app.include_router(users_router, prefix="/users", tags=["users"])