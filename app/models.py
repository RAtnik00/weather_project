from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, UTC
from app.db import Base

class WeatherQuery(Base):
    __tablename__ = "weather_queries"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(UTC))