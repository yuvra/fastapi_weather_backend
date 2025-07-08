from fastapi import APIRouter
from fastapi_weather_backend.services.firebase_config import db
from fastapi_weather_backend.services.weather_fetcher import fetch_rahimatpur_weather

router = APIRouter()

@router.post("/fetch-and-store")
async def fetch_and_store():
    data = await fetch_rahimatpur_weather()
    doc_ref = db.collection("weather_readings").add(data)
    return {"status": "success", "stored": data}