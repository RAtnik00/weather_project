import os
from app.config import DATABASE_URL
from app.db import Base, engine
from sqlalchemy import inspect
from app.models import WeatherQuery  # Важно!

print("Current working directory:", os.getcwd())
print("Database URL:", DATABASE_URL)

Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
print("Tables created:", inspector.get_table_names())




