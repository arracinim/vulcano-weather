from functions.weather import calculate_weather
from models.planet import Planet
from models.coordinates import Coordinates


def test_alligned_and_sun_alligned_planets_response():
    planets = [
        Planet(name="Ferengi", radius=500, angular_speed=1, coordinates=Coordinates(x=500, y=0), clockwise=1),
        Planet(name="Vulcano", radius=1000, angular_speed=5, coordinates=Coordinates(x=-1000, y=0), clockwise=-1),
        Planet(name="Betasoide", radius=2000, angular_speed=3, coordinates=Coordinates(x=2000, y=0), clockwise=1)]
    weather = calculate_weather(planets)
    assert weather == "sequia"


def test_alligned_and_not_sun_alligned_planets_response():
    planets = [
        Planet(name="Ferengi", radius=500, angular_speed=1, coordinates=Coordinates(x=500, y=1), clockwise=1),
        Planet(name="Vulcano", radius=1000, angular_speed=5, coordinates=Coordinates(x=-1000, y=1), clockwise=-1),
        Planet(name="Betasoide", radius=2000, angular_speed=3, coordinates=Coordinates(x=2000, y=1), clockwise=1)]
    weather = calculate_weather(planets)
    assert weather == "optimo"


def test_triangle_with_sun_inside_and_perimeter_is_not_max():
    planets = [
        Planet(name="Ferengi", radius=5, angular_speed=1, coordinates=Coordinates(x=5, y=5), clockwise=1),
        Planet(name="Vulcano", radius=10, angular_speed=5, coordinates=Coordinates(x=-10, y=-10), clockwise=-1),
        Planet(name="Betasoide", radius=20, angular_speed=3, coordinates=Coordinates(x=20, y=-20), clockwise=1)]
    weather = calculate_weather(planets)
    assert weather == "lluvia"


def test_triangle_with_sun_outside_and_perimeter_is_not_max():
    planets = [
        Planet(name="Ferengi", radius=5, angular_speed=1, coordinates=Coordinates(x=5, y=5), clockwise=1),
        Planet(name="Vulcano", radius=10, angular_speed=5, coordinates=Coordinates(x=-10, y=1), clockwise=-1),
        Planet(name="Betasoide", radius=20, angular_speed=3, coordinates=Coordinates(x=20, y=1), clockwise=1)]
    weather = calculate_weather(planets)
    assert weather == "no especificado"


def test_triangle_with_sun_inside_and_perimeter_is_max():
    planets = [
        Planet(name="Ferengi", radius=500, angular_speed=1, coordinates=Coordinates(x=0, y=500), clockwise=1),
        Planet(name="Vulcano", radius=1000, angular_speed=5, coordinates=Coordinates(x=-1000, y=0), clockwise=-1),
        Planet(name="Betasoide", radius=2000, angular_speed=3, coordinates=Coordinates(x=2000, y=0), clockwise=1)]
    weather = calculate_weather(planets)
    assert weather == "lluvia intensa"
