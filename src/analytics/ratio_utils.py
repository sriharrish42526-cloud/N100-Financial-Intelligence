"""
ratio_utils.py

Utility functions for Ratio Engine
"""

from typing import Optional


def safe_divide(numerator: float, denominator: float) -> Optional[float]:
    """
    Safely divide two numbers.

    Returns:
        None if denominator is zero.
    """

    if denominator == 0:
        return None

    return numerator / denominator


def round2(value: Optional[float]) -> Optional[float]:
    """
    Round to 2 decimal places.
    """

    if value is None:
        return None

    return round(value, 2)


def percentage(value: Optional[float]) -> Optional[float]:
    """
    Convert decimal to percentage.
    """

    if value is None:
        return None

    return round(value * 100, 2)