"""
normaliser.py

Contains functions to clean and standardize data
before loading into the database.
"""

import re


def normalize_year(value):
    """
    Convert different year formats into a 4-digit integer.

    Examples:
    ---------
    2024 -> 2024
    "2024" -> 2024
    "FY24" -> 2024
    "FY2023" -> 2023
    "2024 " -> 2024
    """

    if value is None:
        raise ValueError("Year cannot be None")

    text = str(value).strip().upper()

    text = text.replace("FY", "")

    if len(text) == 2:
        return 2000 + int(text)

    if re.fullmatch(r"\d{4}", text):
        return int(text)

    raise ValueError(f"Invalid year: {value}")


def normalize_ticker(value):
    """
    Standardize stock ticker.

    Examples:
    ---------
    " infy " -> "INFY"
    "tcs" -> "TCS"
    """

    if value is None:
        raise ValueError("Ticker cannot be None")

    ticker = str(value).strip().upper()

    if ticker == "":
        raise ValueError("Ticker cannot be empty")

    return ticker