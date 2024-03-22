from enum import Enum

fixed_rate = 0.069
list_of_users = []
current_user = None
current_bank_account_number = 0
user_input = 7

def main():
    print("Welcome to simple bank!")
    print("What would you like to do?\n")

    while True:
        print("For printing the list of users, enter 1\n")
        print("For adding a new user, enter 2\n")
        print("For deposit, enter 3\n")
        print("For withdrawal, enter 4\n")
        print("For info about binding your savings, enter 5\n")
        print("For info about loan repayment, enter 6\n")
        print("For exit the bank, enter 7\n")

        user_input = (input("\nPlease, enter the number: "))
        if user_input.isalpha():
                print("You must enter a number")
                bank_try_again()
        else:
            user_input = int(user_input)
            if user_input <= 0 or user_input > 7:
                print("The number you entered is not valid!\n")
                bank_try_again()
            if user_input == 1:
                print("Users in our bank are: \n")
                looping_trough_users_lists()
                select_current_user()
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
                loan_info()
                bank_question()
            if user_input == 7:
                print("\nThank you for using our services!")
                print("Have a nice day!")
                break


class User():
    def __init__(self, fname, lname, address, account):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account = account
        

    def __str__(self):
        return f"Name: {self.fname} {self.lname} \nAddress: {self.address} \nUser account: {self.account}"


class Account():
    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def __str__(self):
        return f"{self.account_number} {self.account_balance}"
    
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            return Result(self.account_balance, TransactionStatus.FAILED)
        else:
            self.account_balance += deposit_amount
            return (self.account_balance, TransactionStatus.SUCCEEDED)
            
        
    def withdraw(self, withdraw_amount):
        if self.account_balance == 0:
            return Result(self.account_balance, TransactionStatus.FAILED)
        if withdraw_amount > 0 and withdraw_amount <= self.account_balance:
            self.account_balance -= withdraw_amount
            return Result(self.account_balance, TransactionStatus.SUCCEEDED)
        else:
            return Result(self.account_balance, TransactionStatus.FAILED)


class Credit():
    def __init__(self, margin):
        self.margin = margin

    def __str__(self):
        return f"{self.margin}"
    
    def saving_info(self, amt, months):
        self.margin = 0.01
        interest = fixed_rate + self.margin
        new_interest = 0
        for i in range(months):
            amt += amt * interest
            new_interest += interest
        return f"After binding {amt} $ for {months} months your interest will be {new_interest}"
    
    def loan_info(self, amt, months):
        self.margin = 0.02
        monthly_repayment = amt * (fixed_rate + self.margin) * (1 + fixed_rate + self.margin)** months / (1 + fixed_rate + self.margin)** months - 1
        print(f"Your monthly repayment amount will be", round(monthly_repayment, 2), "$")

        for months in range(months):
            amt -= monthly_repayment
            if amt > monthly_repayment:
                print(f"After", months + 1, "month your loan is:", end=" ")
                print(int(amt), "$")
            elif amt > 0:
                print(f"After", months + 1, "month your loan is:", end=" ")
                print(int(amt), "$")
            else:
                print(f"After", months + 1, "month you succeesfully repayed your loan!")
                break
    

class TransactionStatus(Enum):
    FAILED = 1
    SUCCEEDED = 2


class Result():
    def __init__(self, balance, status):
        self.balance = balance
        self.status = status


def bank_question():
    print("\nIs there anything else you would like to do?\n------------\n")


def bank_try_again():
    print("\nPlease try again!\n------------\n")


def looping_trough_users_lists():
    num = 1
    for u in list_of_users:
        print(f"{num} user:\n{u}\n")
        num += 1
        

def select_current_user():
    user = int(input("Select current user: "))
    length = len(list_of_users)
    if user <= 0 or user > length:
        print("\nThe number you entered is not valid!\n")
        bank_try_again()
    else:
        print(f"\n{list_of_users[user-1]}")
        global current_user 
        current_user = list_of_users[user-1]


def creating_new_user():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    address = input("Enter your address: ")
    global current_bank_account_number
    current_bank_account_number = current_bank_account_number + 1
    account = Account(current_bank_account_number, account_balance=0)
    user = User(fname, lname, address, account)
    list_of_users.append(user)


def handle_deposit():
    deposit_amount = int(input("Enter ammount you would like to deposit: ")) 
    deposit_result = current_user.account.deposit(deposit_amount)  
    if deposit_result[-1] == TransactionStatus.FAILED: 
        print(f"Your account balance is {deposit_result[0]} $. Transaction Failed!")
    elif deposit_result[-1] == TransactionStatus.SUCCEEDED:
        print(f"Transaction Succeeded! You made a deposit of {deposit_amount} $. Your account balance is now {deposit_result[0]} $.")


def handle_withdraw():
    withdraw_amount = int(input("Enter ammount you would like to withdraw: "))
    withdraw_result = current_user.account.withdraw(withdraw_amount)
    if withdraw_result.status == TransactionStatus.FAILED:
        print(f"Your account balance is {withdraw_result.balance} $. Transaction Failed!")
    elif withdraw_result.status == TransactionStatus.SUCCEEDED:
        print(f"Transaction Succeeded! You made a withdrawal of {withdraw_amount} $. Your account balance is now {withdraw_result.balance} $.")


def handle_saving_info():
    amt = int(input("Enter the amount you would like to bind: "))
    months = int(input("Enter number of months for binding: "))
    result_info = Credit.saving_info(amt, months)
    #print(f"After binding {amt} $ for {months} months you will have {result_info.amt} $, of which interest will be {result_info.new_interest}")
    print(result_info)

def handle_loan_info():
    amt = int(input("Enter the amount you would like to loan: "))
    months = int(input("Enter for how many months you would like to make a loan: "))
    result_loan = Credit.loan_info(amt, months)





if __name__ == "__main__":
    main()