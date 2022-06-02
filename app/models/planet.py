import math
from pydantic import BaseModel

from app.models.coordinates import Coordinates
from app.utils.constants import circumference_degrees


class Planet(BaseModel):
    name: str
    radius: float
    angular_speed: float
    coordinates: Coordinates

    def __int__(self, name, radius, angular_speed, coordinates):
        self.angular_speed = angular_speed
        self.name = name
        self.radius = radius
        self.coordinates = coordinates

    def getCoordinates(self, day: int) -> Coordinates:
        """
        Given a day, set the coordinates of the planet and return the position values

        :param day: integer value with the day
        :return: coordinates of the planet given the day
        """
        degrees = circumference_degrees - (day * self.angular_speed % circumference_degrees)
        self.coordinates.x = math.floor(self.radius * math.cos(degrees * math.pi / 180))
        self.coordinates.y = math.floor(self.radius * math.sin(degrees * math.pi / 180))
        return self.coordinates
