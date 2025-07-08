from fastapi import APIRouter
from ..models.sensor_data import SensorData
from datetime import datetime

router = APIRouter()

@router.post("/submit")
async def submit_data(data: SensorData):
    # Simulate timestamp generation
    data.timestamp = data.timestamp or datetime.utcnow()
    # Print or log to simulate DB push
    print("✅ Data received:", data)
    return {"message": "Data received successfully", "data": data}
