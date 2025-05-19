from django.db.models.expressions import result
from fastapi import FastAPI, HTTPException, Query
from app.weather_client import WeatherClient
from app.db import SessionLocal
from app.models import WeatherQuery

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Weather API is running"}

@app.get("/weather")
def get_weather(city: str = Query(..., min_length=1)):
    try:
        client = WeatherClient()
        result = client.get_weather(city)
        db = SessionLocal()
        query = WeatherQuery(
            city=result["city"],
            temperature=result["temperature"],
            description=result["description"]
        )
        db.add(query)
        db.commit()
        db.close()
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")