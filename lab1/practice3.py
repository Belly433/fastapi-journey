# ============================================================
# Practice 3 — Defining the Root Endpoint
# ============================================================

# Import FastAPI
from fastapi import FastAPI

# Create app instance
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Greetings from your FastAPI spaceship!"}