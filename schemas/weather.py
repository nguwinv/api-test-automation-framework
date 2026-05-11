from pydantic import BaseModel
from typing import List

class WeatherDescription(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class MainWeather(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

class Wind(BaseModel):
    speed: float
    deg: int

class WeatherResponse(BaseModel):
    name: str
    weather: List[WeatherDescription]
    main: MainWeather
    wind: Wind
    cod: int
