import pytest
from utils.client import get_weather

def test_very_long_city_name():
    response = get_weather("a" * 200)
    assert response.status_code in [400, 404]

def test_single_character_city():
    response = get_weather("a")
    assert response.status_code in [200, 404]

def test_city_with_numbers():
    response = get_weather("London123")
    assert response.status_code in [400, 404]

def test_city_with_spaces():
    response = get_weather("New York")
    assert response.status_code == 200

def test_city_with_hyphen():
    response = get_weather("Stratford-upon-Avon")
    assert response.status_code == 200

def test_city_case_insensitive():
    upper = get_weather("LONDON")
    lower = get_weather("london")
    assert upper.status_code == 200
    assert lower.status_code == 200
    assert upper.json()["name"].lower() == lower.json()["name"].lower()
