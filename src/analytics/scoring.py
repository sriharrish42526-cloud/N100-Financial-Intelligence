"""
scoring.py

Company Quality Scoring Engine
Sprint 2
"""

from typing import Optional


def score_net_profit_margin(value: Optional[float]) -> int:

    if value is None:
        return 0

    if value >= 20:
        return 25

    if value >= 15:
        return 20

    if value >= 10:
        return 15

    if value >= 5:
        return 10

    return 5


def score_debt_to_equity(value: Optional[float]) -> int:

    if value is None:
        return 0

    if value <= 0.5:
        return 25

    if value <= 1:
        return 20

    if value <= 2:
        return 15

    if value <= 3:
        return 10

    return 5


def score_asset_turnover(value: Optional[float]) -> int:

    if value is None:
        return 0

    if value >= 2:
        return 25

    if value >= 1.5:
        return 20

    if value >= 1:
        return 15

    if value >= 0.5:
        return 10

    return 5


def score_eps(value: Optional[float]) -> int:

    if value is None:
        return 0

    if value >= 100:
        return 25

    if value >= 50:
        return 20

    if value >= 20:
        return 15

    if value >= 10:
        return 10

    return 5


def company_score(
    npm,
    de,
    turnover,
    eps
):

    score = (
        score_net_profit_margin(npm)
        + score_debt_to_equity(de)
        + score_asset_turnover(turnover)
        + score_eps(eps)
    )

    return score


def company_rating(score):

    if score >= 90:
        return "★★★★★"

    if score >= 75:
        return "★★★★☆"

    if score >= 60:
        return "★★★☆☆"

    if score >= 40:
        return "★★☆☆☆"

    return "★☆☆☆☆" 