# ============================================================
# Practice 2 — Running FastAPI via Python Script
# ============================================================

# Import FastAPI
from fastapi import FastAPI

# Import uvicorn
import uvicorn

# Create FastAPI app
app = FastAPI()

# Simple route
@app.get("/")
def home():
    return {"message": "hello practice2"}

# Run server using Python script
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)