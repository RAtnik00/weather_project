from app.config import OPENWEATHER_API_KEY

class WeatherClient:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        pass

    def get_weather(self, city: str) -> dict:

        pass