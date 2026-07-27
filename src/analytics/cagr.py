"""
CAGR Engine
Sprint 2
"""

from typing import Optional
import math


def calculate_cagr(start: float, end: float, years: int) -> Optional[float]:
    """
    Calculate CAGR.

    Returns:
        CAGR percentage rounded to 2 decimals
        or None for invalid cases.
    """

    if years <= 0:
        return None

    if start <= 0:
        return None

    if end <= 0:
        return None

    cagr = (math.pow(end / start, 1 / years) - 1) * 100

    return round(cagr, 2)


def revenue_cagr(start, end, years):
    return calculate_cagr(start, end, years)


def pat_cagr(start, end, years):
    return calculate_cagr(start, end, years)


def eps_cagr(start, end, years):
    return calculate_cagr(start, end, years)