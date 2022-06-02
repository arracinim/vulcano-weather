from pydantic import BaseModel


class DayWeather(BaseModel):
    day: int
    weather: str

    class Config:
        orm_mode = True
