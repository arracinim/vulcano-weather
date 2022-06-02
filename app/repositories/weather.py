from sqlalchemy.orm import Session

from app.database.schemas import Weather
from app.models.dayWeather import DayWeather


def getWeather(db: Session):
    return db.query(Weather).all()


def getWeatherByDay(db: Session, day: int):
    return db.query(Weather).filter(Weather.day == day).first()


def insertWeather(db: Session, singleWeather: DayWeather):
    db_singleWeather = Weather(day = singleWeather.day, weather = singleWeather.weather)
    db.add(db_singleWeather)
    db.commit()
    db.refresh(db_singleWeather)
    return db_singleWeather
