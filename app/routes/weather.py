from fastapi import APIRouter, HTTPException, Depends
from pydantic import Json
from sqlalchemy.orm import Session

from app.database.database import Base, engine, SessionLocal
from app.functions.forecastWeather import forecastSingleDayWeather
from app.repositories.weather import getWeather, getWeatherByDay, insertWeather
from app.utils.constants import ten_years

weather = APIRouter()
Base.metadata.create_all(bind=engine)


def get_db():
    """
    :return: db local session of the DB
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@weather.get("/weather/forecast")
def setWeatherRouter(db: Session = Depends(get_db)) -> Json:
    """
    Forecast the weather for ten years and save it in DB

    :param db: Session
    :return: Json
    """
    if getWeather(db):
        pass
    else:
        for i in range(0, ten_years):
            singleDayWeather = forecastSingleDayWeather(i)
            insertWeather(db, singleDayWeather)
    return {"response": "weather was forecasted"}


@weather.get("/weather")
def getWeatherRouter(db: Session = Depends(get_db)) -> Json:
    """
    fetch all DayWeather instances in the DB

    :param db: Session
    :return: DayWeather list
    """
    weatherList = getWeather(db)
    if weatherList:
        return weatherList
    else:
        raise HTTPException(status_code=400, detail="No weather information found")


@weather.get("/weather/{day}")
def getSingleDayWeatherRouter(day: int, db: Session = Depends(get_db)) -> Json:
    """
    Return a DayWeather for a given day if exists

    :param day: int
    :param db: Session
    :return: Json a DayWeather instance
    """
    weatherDay = getWeatherByDay(db, day)
    if weatherDay:
        return weatherDay
    else:
        raise HTTPException(status_code=400, detail=f"There is no predicted climate for the day:  {day}")
