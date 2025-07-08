from fastapi import FastAPI
import asyncio
from fastapi_weather_backend.routes import weather, sensor
from fastapi_weather_backend.services.weather_fetcher import fetch_rahimatpur_weather
from fastapi_weather_backend.services.firebase_config import db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Farmer Assist Weather API"}

app.include_router(weather.router, prefix="/weather")
app.include_router(sensor.router, prefix="/sensor")

@app.on_event("startup")
async def start_background_task():
    asyncio.create_task(push_data_every_5_minutes())


async def push_data_every_5_minutes():
    while True:
        try:
            data = await fetch_rahimatpur_weather()
            db.collection("weather_readings").add(data)
            print("✅ Pushed weather data to Firebase")
        except Exception as e:
            print("❌ Error pushing weather data:", e)

        await asyncio.sleep(300)  # 5 minutes