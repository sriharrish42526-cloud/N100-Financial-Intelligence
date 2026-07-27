from src.analytics.scoring import *


def test_profit_score():
    assert score_net_profit_margin(25) == 25


def test_de_score():
    assert score_debt_to_equity(0.4) == 25


def test_turnover_score():
    assert score_asset_turnover(2.1) == 25


def test_eps_score():
    assert score_eps(120) == 25


def test_company_score():
    assert company_score(25, 0.4, 2.1, 120) == 100


def test_rating():
    assert company_rating(100) == "★★★★★"