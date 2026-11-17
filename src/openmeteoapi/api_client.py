from openmeteoapi.config import KRK_URL
import httpx
from datetime import datetime


def fetch_current_weather() -> dict:
    url = KRK_URL

    params = {
        "latitude": 50.06,
        "longitude": 19.94,
        "current": "temperature_2m,relative_humidity_2m",
        "timezone": "Europe/Warsaw",
    }
    response = httpx.get(url=url, timeout=10.0, params=params)

    response.raise_for_status()
    data = response.json()
    time = data["current"]["time"]
    time = datetime.fromisoformat(time).strftime("%d-%m-%Y %H:%M")
    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    result = {"time": time, "temperature": temperature, "humidity": humidity}

    return result
