import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str, api_key: str = API_KEY, units: str = "metric"):
    return requests.get(BASE_URL, params={
        "q": city,
        "appid": api_key,
        "units": units
    })
