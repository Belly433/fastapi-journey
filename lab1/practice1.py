# Import FastAPI
from fastapi import FastAPI

# Create app instance (use your name)
belly = FastAPI()

# Simple route
@belly.get("/")
def read_root():
    return {"message": "Hello from Practice 1"}