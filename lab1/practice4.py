# ============================================================
# Practice 4 — Path & Query Parameters
# ============================================================

from fastapi import FastAPI

# Initialize a FastAPI app instance
app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob",   "role": "Scientist"},
]

# Endpoint with PATH parameter
@app.get("/crew_with_path/{crew_id}")
def get_crew_with_path(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"message": "Crew member not found"}


# Endpoint with QUERY parameter
@app.get("/crew_with_query/member")
def get_crew_with_query(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"message": "Crew member not found"}