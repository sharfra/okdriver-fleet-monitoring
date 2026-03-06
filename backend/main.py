from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

fleet_data = {
    "total_trips": 1,
    "live_drivers": set(),
    "violations": 0,
    "risk_score": 0
}

class DriverEvent(BaseModel):
    driver_id: str
    event_type: str
    value: float


@app.post("/ingest")
async def ingest_event(event: DriverEvent):

    fleet_data["live_drivers"].add(event.driver_id)

    if event.event_type != "normal":
        fleet_data["violations"] += 1
        fleet_data["risk_score"] += 10

    data = {
        "driver_id": event.driver_id,
        "event_type": event.event_type,
        "value": event.value,
        "violations": fleet_data["violations"],
        "risk_score": fleet_data["risk_score"],
        "live_drivers": len(fleet_data["live_drivers"]),
        "total_trips": fleet_data["total_trips"]
    }

    await manager.broadcast(json.dumps(data))

    return {"status": "event broadcasted"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
