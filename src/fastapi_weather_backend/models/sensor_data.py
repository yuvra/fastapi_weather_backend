from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Location(BaseModel):
    lat: float = Field(..., example=17.5987)
    lng: float = Field(..., example=74.2109)

class SensorData(BaseModel):
    device_id: str = Field(..., example="esp32-rahimatpur-001")
    temperature: float = Field(..., example=28.5)
    humidity: float = Field(..., example=76.0)
    rain_detected: bool = Field(..., example=False)
    soil_moisture: float = Field(..., example=48.3)
    location: Location
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)
