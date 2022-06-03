from pydantic import BaseModel


class Period(BaseModel):
    weather: str
    periods: int

    class Config:
        orm_mode = True
