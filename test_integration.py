import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    balance_from = 1000
    balance_to = 500
    amount = 300

    balance_from, balance_to = transfer(balance_from, balance_to, amount)

    assert balance_from == 700
    assert balance_to == 800


def test_transfer_insufficient_balance():
    balance_from = 200
    balance_to = 500
    amount = 400

    with pytest.raises(ValueError):
        transfer(balance_from, balance_to, amount)


def test_transfer_then_interest():
    balance_from = 2000
    balance_to = 1000
    amount = 500

    balance_from, balance_to = transfer(balance_from, balance_to, amount)

    rate = 10
    years = 1

    final_balance = calculate_interest(balance_to, rate, years)

    assert round(final_balance, 2) == 1650.00
