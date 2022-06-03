from sqlalchemy import func
from sqlalchemy.orm import Session

from database.schemas import Weather
from models.dayweather import DayWeather
from models.periods import Period


def get_weather(db: Session):
    """
    fetch all the DayWeathers instances saved in the DB

    :param db: Session
    :return: list of DayWeathers
    """
    return db.query(Weather).all()


def get_weather_by_day(db: Session, day: int):
    """
    given a day return the DayWeather object if in the DB

    :param db: Session
    :param day: Day of the year
    :return:
    """
    return db.query(Weather).filter(Weather.day == day).first()


def insert_weather(db: Session, singleWeather: DayWeather):
    """
    Insert a new DayWeather object in the DB

    :param db: Session
    :param singleWeather: DayWeather object
    :return: Weather Object
    """
    db_singleWeather = Weather(day=singleWeather.day, weather=singleWeather.weather)
    db.add(db_singleWeather)
    db.commit()
    db.refresh(db_singleWeather)
    return db_singleWeather


def get_weather_periods(db: Session):
    """
    Return the count of the weather periods

    :param db: Session
    :return: Weather Periods
    """
    sql_result = db.query(Weather.weather, func.count(Weather.day).label('periods')).group_by(Weather.weather).all()
    return [Period(weather = x[0], periods= x[1]) for x in sql_result]
