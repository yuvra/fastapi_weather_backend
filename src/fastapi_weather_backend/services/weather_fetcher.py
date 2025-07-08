import httpx
from datetime import datetime, timezone

async def fetch_rahimatpur_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=17.5987&longitude=74.2109"
        "&hourly=temperature_2m,relative_humidity_2m,rain"
        "&timezone=auto"
    )

    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.get(url)
        res.raise_for_status()
        data = res.json()

    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    humidity = hourly.get("relative_humidity_2m", [])
    rain = hourly.get("rain", [])

    if not (times and temps and humidity and rain):
        raise ValueError("Missing expected fields in weather response")

    # Get the most recent index (latest available hour)
    latest_index = len(times) - 1

    return {
        "device_id": "esp32-rahimatpur-001",
        "temperature": temps[latest_index],
        "humidity": humidity[latest_index],
        "rain_detected": rain[latest_index] > 0,
        "soil_moisture": 48.3,  # dummy
        "location": {
            "lat": 17.5987,
            "lng": 74.2109
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
