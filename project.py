from datetime import date
from enum import Enum

fixed_rate = 0.069
list_of_users = []
user_input = 7

def main():
    print("Welcome to simple bank!")
    print("What would you like to do?\n")

    while True:
        print("For printing the list of users, enter 1\n")
        print("For adding a new user, enter 2\n")
        print("For deposit, enter 3\n")
        print("For withdrawal, enter 4\n")
        print("For binding your savings, enter 5\n")
        print("For making a loan, enter 6\n")
        print("For exit the bank, enter 7\n")

        user_input = input("\nPlease, enter the number: ")
        if user_input.isalpha():
                print("You must enter a number")
                bank_try_again()
        else:
            user_input = int(user_input)
            if user_input <= 0 or user_input > 7:
                print("The number you entered is not valid!\n")
                bank_try_again()
            if user_input == 1:
                print(f"Users in our bank are: \n")
                bank_question()
            if user_input == 2:
                creating_new_user()
                print("You successfully added a new user.\n")
                bank_question()
            if user_input == 3:
                handle_deposit()
                bank_question()
            if user_input == 4:
                handle_withdraw()
                bank_question()
            if user_input == 5:
                handle_saving_info()
                bank_question()
            if user_input == 6:
                handle_loan_info()
                bank_question()
            if user_input == 7:
                print("\nThank you for using our services!")
                print("Have a nice day!")
                break


class User():
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address

    def __str__(self):
        return f"{self.fname} {self.lname} {self.address}"


class Account():
    def __init__(self, account_number, account_balance, user):
        self.account_number = account_number
        self.account_balance = account_balance
        self.user = user

    def __str__(self):
        return f"{self.account_number} {self.account_balance}"
    
    def deposit(self, deposit_amount):
        deposit_amount = int(input("Enter ammount you would like to deposit: "))
        if deposit_amount <= 0:
            return (self.account_balance, TransactionStatus.FAILED)
        else:
            self.account_balance += deposit_amount
            return (self.account_balance, TransactionStatus.SUCCEEDED)
            
        
    def withdraw(self, withdraw_amount):
        withdraw_amount = int(input("Enter ammount you would like to withdraw: "))
        if self.account_balance == 0:
            return (self.account_balance, TransactionStatus.FAILED)
        if withdraw_amount > 0 and withdraw_amount <= self.account_balance:
            self.account_balance -= withdraw_amount
            return (self.account_balance, TransactionStatus.SUCCEEDED)
        else:
            return (self.account_balance, TransactionStatus.FAILED)


class Credit():
    def __init__(self, margin):
        self.margin = margin

    def __str__(self):
        return f"{self.margin}"
    
    def saving_info(self, amt, months):
        amt = int(input("Enter the amount you would like to bind: "))
        months = int(input("Enter number of months for binding: "))
        balance = Account.account_balance
        self.margin = 0.01
        for i in range(months):
            amt += amt * fixed_rate * self.margin
        balance += amt
        return (Account.account_balance, TransactionStatus.SUCCEEDED)
    
    def loan(self, amt, months):
        amt = int(input("Enter the amount you would like to loan: "))
        months = int(input("Enter for how many months you would like to make a loan: "))
        self.margin = 0.02
        pass
        file = open("table.csv", "w")
        file.write("Repayment schedule")
        payment = ammount * (int_rate * 100) / time

        date = date.today()

        while payment > 0:
            payment -= payment
            
            print(f"Your payment for")
    

class TransactionStatus(Enum):
    FAILED = 1
    SUCCEEDED = 2


def bank_question():
    print("\nIs there anything else you would like to do?\n------------\n")


def bank_try_again():
    print("\nPlease try again!\n------------\n")


def looping_trough_users_lists():
    for u in list_of_users:
        print(f"{u}\n")


def creating_new_user():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    address = input("Enter your address: ")
    user = User(fname, lname, address)
    list_of_users.append(user)


def handle_deposit(amount):
    deposit_result = Account.deposit(amount)  
    if deposit_result[-1] == TransactionStatus.FAILED: 
        print(f"Your account balance is {Account.account_balance} $. Transaction Failed!")
    elif deposit_result[-1] == TransactionStatus.SUCCEEDED:
        print(f"Transaction Succeeded! You made a deposit of {amount} $. Your account balnce is now {Account.account_balance} $.")


def handle_withdraw(account, amount):
    #result = account.withdraw(amount)
    #if (result.status == Status.Fail)
    pass


def handle_saving_info():
    pass


def handle_loan_info():
    pass


if __name__ == "__main__":
    main()