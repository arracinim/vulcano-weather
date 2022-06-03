from fastapi import APIRouter, HTTPException, Depends
from pydantic import Json
from sqlalchemy.orm import Session

from database.database import Base, engine, SessionLocal
from functions.forecast_weather import forecast_single_day_weather
from repositories.weather import get_weather, get_weather_by_day, insert_weather, get_weather_periods
from utils.constants import ten_years

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


@weather.get("/weather/forecast", name="Forecast Weather",
             summary="Forecast weather for the next 10 years",
             tags=["Weather"],
             responses={
                 200: {
                     "content": {
                         "application/json": {
                             "example": {
                                 "ids": {"response": "weather was forecasted"}}}}}}
             )
def set_weather_router(db: Session = Depends(get_db)) -> Json:
    if get_weather(db):
        pass
    else:
        for i in range(0, ten_years):
            singleDayWeather = forecast_single_day_weather(i)
            insert_weather(db, singleDayWeather)
    return {"response": "weather was forecasted"}


@weather.get("/weather", name="Get Weather",
             summary="Get a list of the forecasted weather in the DB",
             tags=["Weather"],
             responses={
                 200: {
                     "content": {
                         "application/json": {
                             "example":
                                 [{"weather": "optimo", "day": 0}, {"weather": "no especificado", "day": 1},
                                  {"weather": "no especificado", "day": 2}]
                         }}},
                 400: {
                     "content": {
                         "application/json": {
                             "example":
                                 {"detail": "No weather information found"}

                         }
                     }}}
             )
def get_weather_router(db: Session = Depends(get_db)) -> Json:
    weatherList = get_weather(db)
    if weatherList:
        return weatherList
    else:
        raise HTTPException(status_code=400, detail="No weather information found")


@weather.get("/weather/{day}",
             name="Single Day Weather",
             summary="Return the weather for a given single day",
             tags=["Weather"],
             responses={
                 200: {
                     "content": {
                         "application/json": {
                             "example":
                                 {"weather": "no especificado", "day": 1}
                         }}},
                 400: {
                     "content": {
                         "application/json": {
                             "example":
                                 {"detail": "There is no predicted climate for the day:  10000"}
                         }
                     }}}
             )
def get_single_day_weather_router(day: int, db: Session = Depends(get_db)) -> Json:
    weatherDay = get_weather_by_day(db, day)
    if weatherDay:
        return weatherDay
    else:
        raise HTTPException(status_code=400, detail=f"There is no predicted climate for the day:  {day}")


@weather.get("/weather/periods/count", name="Get Weather Periods",
             summary="Return a list of the count of weather periods",
             tags=["Weather"],
             responses={
                 200: {
                     "content": {
                         "application/json": {
                             "example": [{"weather":"lluvia intensa","periods":1080},{"weather":"sequia","periods":10},
                                         {"weather":"no especificado","periods":1790},
                                         {"weather":"lluvia","periods":710},{"weather":"optimo","periods":10}]}}},
                 400: {
                     "content": {
                         "application/json": {
                             "example":
                                 {"detail": "No weather information found"}

                         }
                     }}}
             )
def get_weather_periods_router(db: Session = Depends(get_db)) -> Json:
    weatherPeriodsList = get_weather_periods(db)
    if weatherPeriodsList:
        return weatherPeriodsList
    else:
        raise HTTPException(status_code=400, detail="No weather information found")
