from app.models.dayWeather import DayWeather
from app.utils.planets import planets
from app.functions.weather import calculateWeather


def forecastSingleDayWeather(day: int) -> DayWeather:
    """
    Given a day return the weather of this day

    :param day: Day of the year
    :return: DayWeather instance with the day and the forecasted weather
    """
    for planet in planets:
        planet.getCoordinates(day)
    return DayWeather(
        day=day,
        weather=calculateWeather(planets)
    )


