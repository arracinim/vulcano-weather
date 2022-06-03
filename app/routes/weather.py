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
async def setWeatherRouter(db: Session = Depends(get_db)) -> Json:
    if getWeather(db):
        pass
    else:
        for i in range(0, ten_years):
            singleDayWeather = forecastSingleDayWeather(i)
            await insertWeather(db, singleDayWeather)
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
async def getWeatherRouter(db: Session = Depends(get_db)) -> Json:
    weatherList = await getWeather(db)
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
async def getSingleDayWeatherRouter(day: int, db: Session = Depends(get_db)) -> Json:
    weatherDay = await getWeatherByDay(db, day)
    if weatherDay:
        return weatherDay
    else:
        raise HTTPException(status_code=400, detail=f"There is no predicted climate for the day:  {day}")
