import pytest
from project import User, Account, TransactionStatus


def test_loan_info():
    pass


def test_saving_info():
    pass


def test_user():
    user1 = User("Jack", "London", "Puffington Street 10, London")
    user1.fname == "Jack"
    user1.fname != "Mandy"
    user1.lname == "London"
    user1.lname != "Bond"
    user1.address == "Puffington Street 10, London"
    user1.address != "Brown Street 20, Cardiff"


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
