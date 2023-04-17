# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from datetime import date
from friend import *
from app import app, Loan
import io
import sys
#from oop_loan_pmt import oop_loan_pmt, Loan


# ### unit tests ###
# def test_calculate_current_age():
#     """
#     GIVEN a user enters the year they were born
#     WHEN that year is passed to this function
#     THEN the user's age is accurately calculated
#     """
#     print("\r")  # carriage return
#     print(" -- calculate_current_age unit test")
#     assert (
#         calculate_current_age(2000) == 23
#     )  # STATIC: will change as the years progress


# def test_calculate_current_age():
#     """
#     GIVEN a user enters the year they were born
#     WHEN that year is passed to this function
#     THEN the user's age is accurately calculated
#     """
#     birth_year = 1995
#     today = date.today()
#     expected_age = today.year - birth_year
#     assert (
#         calculate_current_age(birth_year) == expected_age
#     )  # DYNAMIC: calculates the current year

@pytest.fixture
def loan():
    return Loan(100000, 30, 0.06)


# UNIT TESTS
def test_discount_factor_calculation(loan):
    """
    GIVEN your loan information
    WHEN loan infomoation is passed through the calculator
    THEN the discount rate should be matched
    """
    loan.calculateDiscountFactor()
    print("\r")
    print(" -- test discount factor calculation unit test")
    assert loan.getDiscountFactor() == pytest.approx(166.79161439233403, 0.01)


def test_loan_payment_calculation(loan):
    """
    GIVEN your loan information
    WHEN loan infomoation is passed through the calculator
    THEN the loan payment is accurately calculated
    """
    loan.calculateLoanPmt()
    print("\r")
    print(" -- test loan payment calculation unit test")
    assert loan.getLoanPmt() == pytest.approx(599.55, 0.01)

# def test_get_discount_factor(loan):
#     """
#     GIVEN your loan information
#     WHEN loan infomoation is passed through the calculator
#     THEN the discount factor is accurately calculated
#     """
#     loan.calculateDiscountFactor()
#     assert loan.getDiscountFactor() == pytest.approx(169.8125, 0.01)

def test_get_loan_payment(loan):
    """
    GIVEN your loan information
    WHEN loan infomoation is passed through the calculator
    THEN the loan payment is accurately calculated
    """
    loan.calculateLoanPmt()
    print("\r")
    print(" -- test get loan payment unit test")
    assert loan.getLoanPmt() == pytest.approx(599.55, 0.01)

# #FUNCTIONAL TEST
def test_collect_loan_details(monkeypatch):
    """
    GIVEN your loan information
    WHEN loan infomoation is passed through the calculator
    THEN the loan payment is accurately calculated
    """
    inputs = iter(['100000', '30', '0.06'])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    print("\r")
    print(" -- test loan collection details functional test")
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 360
    assert loan.annualRate == 0.06

# def test_collect_loan_details_with_invalid_input(monkeypatch, capsys):
#     inputs = iter(['abc', '30', '0.06', '100000', '30', '0.06'])
#     monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
#     loan = Loan(loanAmount='abc', numberYears=30, annualRate=0.06)
#     print("\r")
#     print(" -- calculateLoanPmt method unit test")
#     assert loan.loanAmount == 100000
#     assert loan.numberOfPmts == 360
#     assert loan.annualRate == 0.06
#     captured = capsys.readouterr()
#     assert 'What is the loan amount?' in captured.out
#     assert 'Please enter a valid loan amount.' in captured.out
#     assert 'What is the loan amount?' in captured.out
#     assert 'How many years is the loan?' in captured.out
#     assert 'What is the annual interest rate for the loan - entered as a decimal?' in captured.out

def test_calculate_loan_pmt_with_zero_loan_amount():
    """
    GIVEN your loan information
    WHEN zero is entered for the loan amount in the calculator
    THEN the loan payment gives back a zero
    """
    loan = Loan(0, 30, 0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt with zero loan amount functional test")
    assert loan.getLoanPmt() == 0


# # integration test
# def test_loan_calculation(capsys):
#     sys.stdin = io.StringIO('100000\n30\n0.06\n')
#     captured = capsys.readouterr()
#     assert 'What is the loan amount?' in captured.out
#     assert 'How many years is the loan?' in captured.out
#     assert 'What is the annual interest rate for the loan - entered as a decimal?' in captured.out
#     assert 'Your monthly payment is: $599.55' in captured.out
