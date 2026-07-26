import pytest

from src.etl.normaliser import normalize_year
from src.etl.normaliser import normalize_ticker


def test_year_int():
    assert normalize_year(2024) == 2024


def test_year_string():
    assert normalize_year("2024") == 2024


def test_year_fy24():
    assert normalize_year("FY24") == 2024


def test_ticker_lower():
    assert normalize_ticker("infy") == "INFY"


def test_ticker_spaces():
    assert normalize_ticker(" reliance ") == "RELIANCE"


def test_invalid_year():
    with pytest.raises(ValueError):
        normalize_year("ABC")


def test_invalid_ticker():
    with pytest.raises(ValueError):
        normalize_ticker("")