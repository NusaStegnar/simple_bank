import pytest
from project import User, Account, TransactionStatus, Credit


def test_get_saving_interest():
    assert Credit.get_saving_interest() == 0.03


def test_get_loan_interest():
    assert Credit.get_loan_interest() == 0.06


def test_get_loan_monthly_repayment():
    assert Credit.get_loan_monthly_repayment(50000, 48, 0.06) == 1174


def test_saving_info():
    assert Credit.saving_info(2000, 12, 0.03) == 60.0


def test_user():
    user1 = User("Jack", "London", "Puffington Street 10, London", 1)
    assert user1.fname == "Jack"
    assert user1.lname == "London"
    assert user1.address == "Puffington Street 10, London"
    assert user1.account == 1


def test_account():
    account1 = Account("123456", 20)
    assert account1.account_number == "123456"
    assert account1.account_balance == 20

    a = account1.deposit(10)
    assert a.balance == 30
    assert a.status == TransactionStatus.SUCCEEDED
   
    b = account1.withdraw(20)
    assert b.balance == 10
    assert b.status == TransactionStatus.SUCCEEDED
    
    c = account1.withdraw(50)
    assert c.status == TransactionStatus.FAILED    
