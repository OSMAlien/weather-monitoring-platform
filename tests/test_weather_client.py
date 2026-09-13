import pytest

from src.weather_client import validate_coordinates


def test_valid_coordinates():
    validate_coordinates(23.5, 58.4)


def test_invalid_latitude():
    with pytest.raises(ValueError):
        validate_coordinates(100, 58.4)


def test_invalid_longitude():
    with pytest.raises(ValueError):
        validate_coordinates(23.5, 300)