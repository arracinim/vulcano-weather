from models.coordinates import Coordinates
from models.planet import Planet

ferengi = Planet(name="Ferengi", radius=500, angular_speed=1, coordinates=Coordinates(x=500, y=0), clockwise=1)
vulcano = Planet(name="Vulcano", radius=1000, angular_speed=5, coordinates=Coordinates(x=1000, y=0), clockwise=-1)
betasoide = Planet(name="Betasoide", radius=2000, angular_speed=3, coordinates=Coordinates(x=2000, y=0), clockwise=1)

planets = [ferengi, vulcano, betasoide]
