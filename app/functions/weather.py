import math

from app.models.coordinates import Coordinates
from app.utils.constants import sun_coordinates, max_triangle_perimeter


def calculateWeather(planets: list) -> str:
    """
    Calculates the weather based on the position of the planets given in the list planets

    :param planets: list of planet instances
    :return: str with the weather
    """
    sunInside = False

    planets_aligned, sun_aligned = aligned(planets)

    # if the planets are not aligned means that they are forming a triangle.
    if not planets_aligned:
        sunInside = sunInsideTriangle(planets, sun_coordinates)

    maxPerimeter = compareMaxPerimeter(calculatePerimeter(planets), max_triangle_perimeter)

    if planets_aligned and sun_aligned:
        return "sequia"
    elif planets_aligned and not sun_aligned:
        return "optimo"
    elif sunInside and maxPerimeter:
        return "lluvia intensa"
    elif sunInside:
        return "lluvia"
    else:
        return "no especificado"


def aligned(planets: list) -> (bool, bool):
    """
    verify if planets are aligned and aligned with the sun

    :param planets: list of instance PLanet
    :return: boolean tuple, at the first position true if they are aligned and if it aligned with sun in the
    second position
    """

    # Calculate the slope and intercept of the line
    if (planets[2].coordinates.x - planets[0].coordinates.x) == 0:
        m = 0.0
    else:
        m = round((planets[2].coordinates.y - planets[0].coordinates.y) /
                  (planets[2].coordinates.x - planets[0].coordinates.x))

    b = round(planets[0].coordinates.y - m * planets[0].coordinates.x)

    # if the coordinates of planet in the middle belongs to the line, it means that
    # the planet is aligned with the others also if the b (intercept with y) is zero,
    # it means that the planets are aligned with the sun

    return planets[1].coordinates.y == (m * planets[1].coordinates.y + b), b == 0.0


def calculatePerimeter(planets: list) -> float:
    """
    Given a list of planets calculate the perimeter of the triangle.

    :param planets: list of planet instances
    :return: the perimeters ot the triangle
    """

    dFB = math.sqrt(math.pow((planets[2].coordinates.x - planets[0].coordinates.x), 2) + math.pow(
        (planets[2].coordinates.y - planets[0].coordinates.y), 2))

    dFV = math.sqrt(math.pow((planets[1].coordinates.x - planets[0].coordinates.x), 2) + math.pow(
        (planets[1].coordinates.y - planets[0].coordinates.y), 2))

    dVB = math.sqrt(math.pow((planets[2].coordinates.x - planets[1].coordinates.x), 2) + math.pow(
        (planets[2].coordinates.y - planets[1].coordinates.y), 2))

    return dFB + dFV + dVB


def sunInsideTriangle(planets: list, sunCoordinates: Coordinates) -> bool:
    """
    Calculate if the sun is inside the triangle formed by the planets

    :param sunCoordinates: Coordinates object
    :param planets: list of planet instances
    :return: True if the sun is inside the triangle
    """

    dX = sunCoordinates.x - planets[2].coordinates.x
    dY = sunCoordinates.y - planets[2].coordinates.y
    dX21 = planets[2].coordinates.x - planets[1].coordinates.x
    dY12 = planets[1].coordinates.y - planets[2].coordinates.y
    D = dY12 * (planets[0].coordinates.x - planets[2].coordinates.x) + \
        dX21 * (planets[0].coordinates.y - planets[2].coordinates.y)
    s = dY12 * dX + dX21 * dY

    t = (planets[2].coordinates.y - planets[0].coordinates.y) * dX + \
        (planets[0].coordinates.x - planets[2].coordinates.x) * dY
    if D < 0:
        return s <= 0 and t <= 0 and s + t >= D
    return s >= 0 and t >= 0 and s + t <= D


def compareMaxPerimeter(perimeter: float, maxPerimeter: float) -> bool:
    """
    Calculate is the perimeter of the triangle is maximum

    :param perimeter: Perimeter of the triangle
    :param maxPerimeter: max perimeter calculated before
    :return: true if the perimeter es maximum
    """
    # In this case we are going to consider the perimeter is maximum when
    # the relation is higher than 0.98
    return perimeter / maxPerimeter > 0.98
