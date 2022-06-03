from sqlalchemy.orm import Session

from app.database.schemas import Weather
from app.models.dayWeather import DayWeather


def getWeather(db: Session):
    """
    fetch all the DayWeathers instances saved in the DB

    :param db: Session
    :return: list of DayWeathers
    """
    return db.query(Weather).all()


def getWeatherByDay(db: Session, day: int):
    """
    given a day return the DayWeather object if in the DB

    :param db: Session
    :param day: Day of the year
    :return:
    """
    return db.query(Weather).filter(Weather.day == day).first()


def insertWeather(db: Session, singleWeather: DayWeather):
    """
    Insert a new DayWeather object in the DB

    :param db: Session
    :param singleWeather: DayWeather object
    :return: Weather Object
    """
    db_singleWeather = Weather(day = singleWeather.day, weather = singleWeather.weather)
    db.add(db_singleWeather)
    db.commit()
    db.refresh(db_singleWeather)
    return db_singleWeather
