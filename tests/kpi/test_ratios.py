import pytest

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)


# -----------------------------
# Net Profit Margin
# -----------------------------
def test_net_profit_margin():
    assert net_profit_margin(100, 500) == 20.00


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


# -----------------------------
# Operating Profit Margin
# -----------------------------
def test_operating_profit_margin():
    assert operating_profit_margin(150, 1000) == 15.00


# -----------------------------
# ROE
# -----------------------------
def test_return_on_equity():
    assert return_on_equity(100, 300, 200) == 20.00


def test_return_on_equity_negative():
    assert return_on_equity(100, -100, 50) is None


# -----------------------------
# ROCE
# -----------------------------
def test_return_on_capital_employed():
    assert return_on_capital_employed(120, 300, 200, 100) == 20.00


# -----------------------------
# ROA
# -----------------------------
def test_return_on_assets():
    assert return_on_assets(100, 500) == 20.00


# -----------------------------
# Debt to Equity
# -----------------------------
def test_debt_to_equity():
    assert debt_to_equity(200, 300, 200) == 0.40


def test_debt_to_equity_debt_free():
    assert debt_to_equity(0, 300, 200) == 0


# -----------------------------
# Interest Coverage
# -----------------------------
def test_interest_coverage():
    assert interest_coverage_ratio(200, 50, 25) == 10.00


def test_interest_zero():
    assert interest_coverage_ratio(200, 50, 0) is None


# -----------------------------
# Asset Turnover
# -----------------------------
def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2.00