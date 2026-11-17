from openmeteoapi.api_client import fetch_current_weather
import httpx, pytest
from unittest.mock import patch, call


@pytest.fixture
def example_correct_data():
    return {
        "latitude": 50.057274,
        "longitude": 19.949356,
        "generationtime_ms": 0.08428096771240234,
        "utc_offset_seconds": 3600,
        "timezone": "Europe/Warsaw",
        "timezone_abbreviation": "GMT+1",
        "elevation": 220.0,
        "current_units": {
            "time": "iso8601",
            "interval": "seconds",
            "temperature_2m": "°C",
            "relative_humidity_2m": "%",
        },
        "current": {
            "time": "2026-11-17T09:45",
            "interval": 900,
            "temperature_2m": 5.4,
            "relative_humidity_2m": 90,
        },
    }


@pytest.fixture
def get_error_500() -> httpx.HTTPStatusError:
    request = httpx.Request(method="GET", url="test")
    response = httpx.Response(status_code=500, request=request)
    return httpx.HTTPStatusError(
        message="Error 500", response=response, request=request
    )


def test_fetch_current_weather_succes(example_correct_data):
    expected_data = {"time": "17-11-2026 09:45", "temperature": 5.4, "humidity": 90}
    with patch("httpx.get") as mock_get:
        mock_get.return_value.json.return_value = example_correct_data
        data = fetch_current_weather()
        mock_get.return_value.raise_for_status.assert_called_once()
        assert data == expected_data


def test_fetch_current_wheather_raises_on_http_500(get_error_500):
    with patch("httpx.get") as mock_get:
        mock_get.return_value.raise_for_status.side_effect = get_error_500
        with pytest.raises(httpx.HTTPStatusError):
            fetch_current_weather()


def test_fetch_current_weather_raises_on_timeout():
    with patch("httpx.get") as mock_get:
        mock_get.side_effect = httpx.ReadTimeout("Timeout reached")
        with pytest.raises(httpx.TimeoutException):
            fetch_current_weather()
