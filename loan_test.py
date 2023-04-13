import pytest
from loan import *

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Unit tests for Loan class
def test_discount_factor():
    """
    GIVEN the user enters their loan details
    WHEN the loan object's calculateDiscountFactor method is called
    THEN the discount factor is accurately calculated
    """
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    print("\r")
    print(" -- calculateDiscountFactor method unit test")
    assert round(loan.getDiscountFactor(), 4) == 166.7916

def test_loan_payment():
    """
    GIVEN the user enters their loan details
    WHEN the loan object's calculateLoanPmt method is called
    THEN the loan payment is accurately calculated
    """
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt method unit test")
    assert round(loan.getLoanPmt(), 2) == 599.55

# Functional tests
def test_collect_loan_details(monkeypatch):
    """
    GIVEN the user enters loan details
    WHEN input details do not match expected details
    THEN overwrite with expected details
    """
    inputs = ["100000", "30", "0.06"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    loan = collectLoanDetails()
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 360
    assert loan.annualRate == 0.06

# Integration test
def test_main_output(capsys, monkeypatch):
    """
    GIVEN get loan details
    WHEN input details do not match expected details
    THEN overwrite with expected details
    """
    inputs = ["100000", "30", "0.06"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    main()
    captured = capsys.readouterr()
    assert captured.out == "Your monthly payment is: $599.55\n"



