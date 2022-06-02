from fastapi import FastAPI
from app.models.planet import Planet
from app.models.coordinates import Coordinates

app = FastAPI()

ferengi = Planet(name="Ferengi", radius=500, angular_speed=1, coordinates=Coordinates(x=0, y=500))
betasoide = Planet(name="Betasoide", radius=2000, angular_speed=3, coordinates=Coordinates(x=0, y=2000))
vulcano = Planet(name="Vulcano", radius=1000, angular_speed=5, coordinates=Coordinates(x=0, y=1000))

planets = [ferengi, betasoide, vulcano]

@app.get('/')
async def index():
    return {"python": "vulcano-weather"}

