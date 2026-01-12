import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


def test_deposit_valid():
    assert deposit(1000, 500) == 1500


def test_deposit_boundary():
    assert deposit(0, 1) == 1


def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)


def test_withdraw_valid():
    assert withdraw(1000, 400) == 600


def test_withdraw_boundary():
    assert withdraw(500, 500) == 0


def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -10)


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)


def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00


def test_calculate_interest_boundary():
    assert calculate_interest(0, 5, 1) == 0


def test_calculate_interest_invalid_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 5, 1)


def test_calculate_interest_invalid_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 1)


def test_loan_eligibility_approved():
    balance = 6000
    credit_score = 750

    result = check_loan_eligibility(balance, credit_score)

    assert result == True


def test_loan_eligibility_rejected():
    balance = 3000
    credit_score = 650

    result = check_loan_eligibility(balance, credit_score)

    assert result == False



def test_loan_eligibility_invalid_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-100, 700)
