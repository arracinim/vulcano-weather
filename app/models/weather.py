from pydantic import BaseModel


class Weather(BaseModel):
    day: int
    weather: str
