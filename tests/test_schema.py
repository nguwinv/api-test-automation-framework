import pytest
from utils.client import get_weather
from schemas.weather import WeatherResponse

def test_response_matches_schema():
    response = get_weather("London")
    assert response.status_code == 200
    WeatherResponse(**response.json())

def test_temperature_fields_are_floats():
    response = get_weather("Tokyo")
    data = response.json()
    main = data["main"]
    assert isinstance(main["temp"], (int, float))
    assert isinstance(main["feels_like"], (int, float))
    assert isinstance(main["temp_min"], (int, float))
    assert isinstance(main["temp_max"], (int, float))

def test_humidity_is_percentage():
    response = get_weather("Sydney")
    humidity = response.json()["main"]["humidity"]
    assert 0 <= humidity <= 100

def test_wind_speed_is_non_negative():
    response = get_weather("Paris")
    wind_speed = response.json()["wind"]["speed"]
    assert wind_speed >= 0

def test_weather_description_not_empty():
    response = get_weather("Berlin")
    descriptions = response.json()["weather"]
    assert len(descriptions) > 0
    assert descriptions[0]["description"] != ""
