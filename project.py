from datetime import date



def main():
    pass

    #new user, new account

    #TODO tests!!!
    #handleDepost()
    #handleWithdraw(account)



class User():
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address

    def __str__(self):
        return f"{self.fname}{self.lname}"


class Account():
    def __init__(self, account_number, account_balance, user):
        self.account_number = account_number
        self.account_balance = account_balance
        self.user = user

    def __str__(self):
        return f"{self.account_number}{self.account_balance}"
    
    def withdraw():
        #TODO refactor to return just status code and current amount
        withdraw_amount = int(input("Enter ammount you would like to withdraw: "))
        balance = account.account_balace

        if balance == 0:
            return f"Balance on your account is 0."
        if withdraw_amount > 0 and withdraw_amount <= balance:
            print(f"Your balace is: {balance} Є")
            balance -= withdraw_amount
            return f"Your balance now is {balance} Є"
        else:
            return f"You don't have enough credit on your account!"


class Credit():
    def __init__(self, int_rate):
        self.int_rate = int_rate

    def __str__(self):
        return f"{self.int_rate}"
    
def handleWithdraw(account, amount):
    #result = account.withdraw(amount)
    #if


    


def deposit():
    deposit_amount = int(input("Enter ammount you would like to deposit: "))
    balance = account.account_balance

    if deposit_amount > 0:
        print(f"Your balace is: {balance} Є")
        balance += deposit_amount
        return f"Your new balance is {balance} Є"


def loan():
    loan = int(input("Enter the amount you would like to borrow: "))
    year = int(input("Enter years of loan: "))
    time = year * 12
    int_rate = credit.int_rate

    print(f"Interest rate for your loan is {int_rate} %")


    file = open("table.csv", "w")
    file.write("Repayment schedule")
    payment = loan * (int_rate * 100) / time

    date = date.today()

    while payment > 0:
        payment -= payment
        
        print(f"Your payment for")


    



def saving():
    amt = int(input("Enter the amount you would like to bind: "))
    years = int(input("Enter year for binding: "))
    balance = account.account_balance
    int_rate = credit.int_rate 

    print(f"Your balance is {balance} Є")
    print(f"You are binding {amt} Є for {years} years with interest rate {int_rate} %")

    for i in range(years):
        amt += amt * (int_rate * 100)
    balance += amt
    return f"After {years} years your balance will be {balance}"










user = User("John", "Doe", "Buffingtone Street 20, Illinois")
account = Account("UA123 548 9874", 15000, user)
credit = Credit(3.75)








if __name__ == "__main__":
    main()