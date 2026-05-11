import pytest
from utils.client import get_weather

def test_invalid_city_returns_404():
    response = get_weather("thiscitydoesnotexist12345")
    assert response.status_code == 404

def test_empty_city_returns_400():
    response = get_weather("")
    assert response.status_code == 400

def test_numeric_city_returns_404():
    response = get_weather("99999")
    assert response.status_code == 404

def test_special_characters_returns_400_or_404():
    response = get_weather("@@@!!!")
    assert response.status_code in [400, 404]

def test_invalid_api_key_returns_401():
    response = get_weather("London", api_key="invalidkey123")
    assert response.status_code == 401
