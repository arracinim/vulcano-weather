import math
from pydantic import BaseModel

from models.coordinates import Coordinates
from utils.constants import circumference_degrees


class Planet(BaseModel):
    name: str
    radius: float
    angular_speed: float
    coordinates: Coordinates
    clockwise: float

    def __int__(self, name, radius, angular_speed, coordinates, clockwise):
        self.angular_speed = angular_speed
        self.name = name
        self.radius = radius
        self.coordinates = coordinates
        self.clockwise = clockwise

    def get_coordinates(self, day: int) -> Coordinates:
        """
        Given a day, set the coordinates of the planet and return the position values

        :param day: integer value with the day
        :return: coordinates of the planet given the day
        """
        degrees = circumference_degrees - (day * self.angular_speed % circumference_degrees) * self.clockwise
        self.coordinates.x = math.floor(self.radius * math.cos(degrees * math.pi / 180))
        self.coordinates.y = math.floor(self.radius * math.sin(degrees * math.pi / 180))
        return self.coordinates
