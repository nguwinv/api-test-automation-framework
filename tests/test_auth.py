import pytest
from utils.client import get_weather

def test_no_api_key_returns_401():
    response = get_weather("London", api_key="")
    assert response.status_code == 401

def test_invalid_api_key_returns_401():
    response = get_weather("London", api_key="totallyFakeKey999")
    assert response.status_code == 401

def test_numeric_api_key_returns_401():
    response = get_weather("London", api_key="123456789")
    assert response.status_code == 401

def test_whitespace_api_key_returns_401():
    response = get_weather("London", api_key="   ")
    assert response.status_code == 401

def test_valid_key_returns_200():
    response = get_weather("London")
    assert response.status_code == 200
