from fastapi import APIRouter, HTTPException
from models.events import Event

router = APIRouter()


@router.get("/")
async def get_events():
    events = await Event.find_all().to_list()
    return events


@router.post("/")
async def create_event(event: Event):
    await event.create()
    return event


@router.get("/{id}")
async def get_event(id: str):
    event = await Event.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{id}")
async def delete_event(id: str):
    event = await Event.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    await event.delete()
    return {"message": "deleted"}