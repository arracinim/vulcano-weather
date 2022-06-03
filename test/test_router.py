from fastapi.testclient import TestClient

from main import app
from utils.constants import ten_years

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
    client.get("/weather/forecast")
    response = client.get("/weather")
    assert response.status_code == 200
    assert len(response.json()) == ten_years


def test_weather_single_day_router():
    client.get("/weather/forecast")
    response = client.get("/weather/1")
    assert response.status_code == 200
    assert response.json() == {"weather": "no especificado", "day": 1}


def test_weather_single_day_bad_request():
    client.get("/weather/forecast")
    response = client.get("/weather/10000")
    assert response.status_code == 400
    assert response.json() == {'detail': 'There is no predicted climate for the day:  10000'}


def test_weather_periods_count():
    client.get("/weather/forecast")
    response = client.get("/weather/periods/count")
    assert response.status_code == 200
    assert response.json() == [{"weather":"lluvia intensa","periods":1080},{"weather":"sequia","periods":10},
                               {"weather":"no especificado","periods":1790},
                               {"weather":"lluvia","periods":710},{"weather":"optimo","periods":10}]
