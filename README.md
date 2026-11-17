# 05 — OpenMeteo API Integration

## Description

A small Python learning project demonstrating integration with an external REST API.

The application retrieves current weather data for Kraków, Poland, using the Open-Meteo API.

It extracts and returns:
- Local date and time
- Temperature in °C
- Relative humidity in %

## Tech Stack

- Python 3.13+
- httpx
- pytest
- uv

## Installation

Install project dependencies:

```bash
uv sync
```

## Usage

Run the weather API client:

```bash
uv run python -c "from openmeteoapi.api_client import fetch_current_weather; print(fetch_current_weather())"
```

Example output:

```python
{
    "time": "17-11-2026 09:45",
    "temperature": 5.4,
    "humidity": 90
}
```

## Testing

Run automated tests:

```bash
uv run pytest -q
```

Tests cover:
- Successful API response and data extraction
- HTTP 500 errors
- Request timeouts

External HTTP requests are mocked during testing.

## Learning Objectives

- Making HTTP GET requests with query parameters
- Working with JSON responses
- Handling HTTP errors and timeouts
- Formatting date and time
- Writing automated tests with pytest and unittest.mock

## Project Status

Completed educational exercise. Not intended as a production weather service.