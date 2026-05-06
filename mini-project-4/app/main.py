from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
print("WEBSOCKET LOADED")
from pydantic import BaseModel
from typing import List

app = FastAPI()


polls = {}
current_id = 1

# WebSocket connections
connections = {}  # { poll_id: [websocket1, websocket2] }



class PollCreate(BaseModel):
    question: str
    options: List[str]


class Vote(BaseModel):
    option_index: int




@app.post("/polls")
def create_poll(poll: PollCreate):
    global current_id

    poll_data = {
        "id": current_id,
        "question": poll.question,
        "options": poll.options,
        "votes": [0] * len(poll.options)
    }

    polls[current_id] = poll_data
    current_id += 1

    return poll_data



@app.get("/polls")
def get_polls():
    return list(polls.values())



@app.get("/polls/{poll_id}")
def get_poll(poll_id: int):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")

    return polls[poll_id]



@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: int):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")

    del polls[poll_id]
    return {"message": "Poll deleted"}



@app.post("/polls/{poll_id}/vote")
def vote_poll(poll_id: int, vote: Vote):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")

    if vote.option_index >= len(polls[poll_id]["options"]):
        raise HTTPException(status_code=400, detail="Invalid option")

    polls[poll_id]["votes"][vote.option_index] += 1

    return polls[poll_id]


@app.websocket("/ws/polls/{poll_id}")
async def websocket_endpoint(websocket: WebSocket, poll_id: int):
    await websocket.accept()

    # initialiser liste connexions
    if poll_id not in connections:
        connections[poll_id] = []

    connections[poll_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            option_index = data.get("option_index")

            if poll_id not in polls:
                await websocket.send_json({"error": "Poll not found"})
                continue

            if option_index is None or option_index >= len(polls[poll_id]["options"]):
                await websocket.send_json({"error": "Invalid option"})
                continue

            # ajouter vote
            polls[poll_id]["votes"][option_index] += 1

            # broadcast à tous
            for conn in connections[poll_id]:
                await conn.send_json(polls[poll_id])

    except WebSocketDisconnect:
        connections[poll_id].remove(websocket)
    