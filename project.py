from datetime import date

fixed_rate = 0.069
list_of_users = []
exit = 7

def main():
    print("Welcome to simple bank!")
    print("What would you like to do?")
    while True:
        print("For printing the list of users, enter 1")
        print("For adding a new user, enter 2")
        print("For deposit, enter 3")
        print("For withdrawal, enter 4")
        print("For binding your savings, enter 5")
        print("For making a loan, enter 6")
        print("For exit the bank, enter 7")
        exit = int(input("\nPlease, enter the number: "))
        if exit <= 0 or exit > 7:
            print("The number you entered is not valid!\n")
            print("Please try again!")
            print("------------\n")
        if exit == 1:
            print(f"Users in our bank are: {list_of_users}\n")
            print("Is there anything else you would like to do?")
            print("------------\n")
        if exit == 2:
            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            address = input("Enter your address: ")
            user = User(fname, lname, address)
            list_of_users.append(user)
            print("You successfully added a new user.\n")
            print("Is there anything else you would like to do?")
            print("------------\n")
        if exit == 3:
            deposit_amount = int(input("Enter ammount you would like to deposit: "))
            deposit_money = handle_deposit(deposit_amount)
            print(deposit(deposit_money))
            print("\nIs there anything else you would like to do?")
            print("------------\n")
        if exit == 4:
            withdraw_amount = int(input("Enter ammount you would like to withdraw: "))
            withdraw_money = handle_withdraw(withdraw_amount)
            print(withdraw(withdraw_money))
            print("\nIs there anything else you would like to do?")
            print("------------\n")
        if exit == 5:
            amt = int(input("Enter the amount you would like to bind: "))
            months = int(input("Enter months for binding: "))
            print(saving(amt,months))
            print("\nIs there anything else you would like to do?")
            print("------------\n")
        if exit == 6:
            amt = int(input("Enter the amount you would like to loan: "))
            months = int(input("Enter for how many months you would like to make a loan: "))
            print(loan(amt, months))
            print("\nIs there anything else you would like to do?")
            print("------------\n")
        if exit == 7:
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
        return f"{self.account_number}{self.account_balance}"
    
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            return {"balance": balance,  "Status": "Failed"}
            #TODO TransactionData(balance, Status.Fail)
        
        self.account_balance += deposit_amount
        
        return {"balance": self.account_balance}
        
    def withdraw(balance, withdraw_amount):
        #TODO refactor to return just status code and current amount
        balance = account.account_balace

        if balance == 0:
            return {"balance": balance,  "Status": "Failed"}
        if withdraw_amount > 0 and withdraw_amount <= balance:
            balance -= withdraw_amount
            return {"balance": balance,  "Status": "Succeeded"}
        else:
            return {"balance": balance,  "Status": "Failed"}
        
    def saving(amt, months):#TODO rename, savingInfo ??
        balance = account.account_balance
        int_rate = credit.int_rate 
        for i in range(months):
            amt += amt * (int_rate * 100)
        balance += amt
        return {"months": months, "balance": balance}


class Credit():
    def __init__(self, int_rate):
        self.int_rate = int_rate

    def __str__(self):
        return f"{self.int_rate}"
    
    def loan(ammount, months):
        time = months
        int_rate = credit.int_rate
        file = open("table.csv", "w")
        file.write("Repayment schedule")
        payment = ammount * (int_rate * 100) / time

        date = date.today()

        while payment > 0:
            payment -= payment
            
            print(f"Your payment for")
    
    
def handle_withdraw(account, amount):
    #result = account.withdraw(amount)
    #if (result.status == Status.Fail)
    pass


def handle_deposit(account, amount):
    pass   


if __name__ == "__main__":
    main()