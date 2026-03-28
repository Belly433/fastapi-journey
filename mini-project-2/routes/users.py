from fastapi import APIRouter, HTTPException
from models.users import User

router = APIRouter()


@router.post("/")
async def create_user(user: User):
    await user.create()
    return user


@router.get("/")
async def get_users():
    users = await User.find_all().to_list()
    return users


@router.get("/{id}")
async def get_user(id: str):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user