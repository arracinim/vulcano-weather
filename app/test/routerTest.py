from fastapi.testclient import TestClient

from app.main import app
from app.utils.constants import ten_years

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"health_check": "up"}


def test_forecast_router():
    response = client.get("/weather/forecast")
    assert response.status_code == 200
    assert response.json() == {"response": "weather was forecasted"}


def test_weather_router():
    response = client.get("/weather")
    assert response.status_code == 200
    assert len(response.json()) == ten_years


def test_weather_single_day_router():
    response = client.get("/weather/1")
    assert response.status_code == 200
    assert response.json() == {"weather": "no especificado", "day": 1}


def test_weather_single_day_bad_request():
    response = client.get("/weather/10000")
    assert response.status_code == 400
    assert response.json() == {'detail': 'There is no predicted climate for the day:  10000'}
