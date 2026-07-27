"""
Cash Flow KPIs
Sprint 2
"""

from typing import Optional


def free_cash_flow(operating_cf, investing_cf):

    return operating_cf + investing_cf


def cfo_quality_score(cfo, pat):

    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1:
        return "High Quality"

    if ratio >= 0.5:
        return "Moderate"

    return "Accrual Risk"


def capex_intensity(investing_cf, sales):

    if sales == 0:
        return None

    value = abs(investing_cf) / sales * 100

    if value < 3:
        return "Asset Light"

    elif value <= 8:
        return "Moderate"

    return "Capital Intensive"


def fcf_conversion(fcf, operating_profit):

    if operating_profit == 0:
        return None

    return round(fcf / operating_profit * 100, 2)


def capital_allocation_pattern(cfo, cfi, cff):

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    mapping = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed"
    }

    return mapping.get(signs, "Unknown")