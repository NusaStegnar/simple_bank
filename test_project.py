import pytest
from project import withdraw, deposit, loan, saving, User, Account, andle_withdraw, handle_deposit


def main():
    test_handle_withdraw()
    test_handle_deposit()
    test_loan_info()
    test_saving_info()


def test_handle_withdraw():
    if withdraw(0, 20):
        return f'0: "Failed"'
    if withdraw(20, 70):
        return '20: "Succeeded"'
    if withdraw(80, 50):
        return f'80: "Failed"'
    

def test_handle_deposit():
    pass


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
    account1.account_number == "123456"
    account1.account_number != "654321"
    account1.account_balance == 20
    account1.account_balance != 50



if __name__ == "__main__":
    main()