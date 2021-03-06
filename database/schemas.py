from sqlalchemy import Column, Integer, String

from database.database import Base


class Weather(Base):
    __tablename__ = "weather"

    day = Column(Integer, primary_key=True)
    weather = Column(String)
