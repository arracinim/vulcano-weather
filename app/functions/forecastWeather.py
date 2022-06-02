from app.models.dayWeather import DayWeather
from app.utils.planets import planets
from app.functions.weather import calculateWeather


def forecastSingleDayWeather(day: int):
    for planet in planets:
        planet.getCoordinates(day)
    return DayWeather(
        day=day,
        weather=calculateWeather(planets)
    )


