import pytest
from utils.client import get_weather

def test_valid_city_returns_200():
    response = get_weather("London")
    assert response.status_code == 200

def test_response_contains_required_fields():
    response = get_weather("London")
    data = response.json()
    assert "main" in data
    assert "weather" in data
    assert "name" in data
    assert "wind" in data

def test_temperature_is_a_number():
    response = get_weather("London")
    temp = response.json()["main"]["temp"]
    assert isinstance(temp, (int, float))

def test_city_name_matches_request():
    response = get_weather("Paris")
    data = response.json()
    assert data["name"].lower() == "paris"

def test_multiple_cities_return_200():
    for city in ["Tokyo", "New York", "Sydney", "Lagos"]:
        response = get_weather(city)
        assert response.status_code == 200, f"Failed for city: {city}"
