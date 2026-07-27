"""
Leverage KPIs
Sprint 2
"""

from typing import Optional


def debt_to_equity(
    borrowings: float,
    equity: float,
) -> Optional[float]:

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return round(borrowings / equity, 2)


def high_leverage_flag(
    debt_to_equity_ratio: Optional[float],
    sector: str
) -> bool:

    if debt_to_equity_ratio is None:
        return False

    if sector == "Financials":
        return False

    return debt_to_equity_ratio > 5