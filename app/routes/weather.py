from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.database import Base, engine, SessionLocal
from app.functions.forecastWeather import forecastSingleDayWeather
from app.repositories.weather import getWeather, getWeatherByDay, insertWeather
from app.utils.constants import ten_years

weather = APIRouter()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@weather.get("/weather/forecast")
def setWeatherRouter(db: Session = Depends(get_db)):
    for i in range(0, ten_years):
        singleDayWeather = forecastSingleDayWeather(i)
        insertWeather(db, singleDayWeather)
    return {"response": "weather was forecasted"}


@weather.get("/weather")
def getWeatherRouter(db: Session = Depends(get_db)):
    weatherList = getWeather(db)
    if weatherList:
        return weatherList
    else:
        raise HTTPException(status_code=400, detail="No weather information found")


@weather.get("/weather/{day}")
def getSingleDayWeatherRouter(day: int, db: Session = Depends(get_db)):
    weatherDay = getWeatherByDay(db, day)
    if weatherDay:
        return weatherDay
    else:
        raise HTTPException(status_code=400, detail=f"There is no predicted climate for the day:  {day}")
