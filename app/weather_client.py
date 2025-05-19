from app.config import OPENWEATHER_API_KEY
import requests

class WeatherClient:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        pass

    def get_weather(self, city: str) -> dict:
        if not city.strip():
            raise ValueError("City name cannot be empty")
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 404:
            raise ValueError("City not found")
        if response.status_code != 200:
            raise Exception("Weather API error")

        data = response.json()
        name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return {
            "city": name,
            "temperature": temperature,
            "description": description
        }