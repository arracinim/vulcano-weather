from models.dayweather import DayWeather
from utils.planets import planets
from functions.weather import calculate_weather


def forecast_single_day_weather(day: int) -> DayWeather:
    """
    Given a day return the weather of this day

    :param day: Day of the year
    :return: DayWeather instance with the day and the forecasted weather
    """
    for planet in planets:
        planet.get_coordinates(day)
    return DayWeather(
        day=day,
        weather=calculate_weather(planets)
    )


