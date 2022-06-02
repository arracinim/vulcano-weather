from app.models.weather import Weather


def calculateWeather(planets : list) -> Weather:
    """
    Calculates the weather based on the position of the planets given in the list planets

    :param planets: List[Planet]
    :return: Weather
    """
    return Weather(1,"sequia")