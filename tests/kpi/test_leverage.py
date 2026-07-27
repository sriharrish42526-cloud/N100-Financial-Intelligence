from src.analytics.leverage import *


def test_debt_free():

    assert debt_to_equity(
        0,
        100
    ) == 0


def test_negative_equity():

    assert debt_to_equity(
        100,
        -50
    ) is None


def test_normal():

    assert debt_to_equity(
        100,
        200
    ) == 0.5


def test_flag():

    assert high_leverage_flag(
        6,
        "IT"
    )


def test_bank():

    assert not high_leverage_flag(
        8,
        "Financials"
    )