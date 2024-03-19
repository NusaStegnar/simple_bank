
fixed_rate = 0.069


def loan_info():
    amt = int(input("Enter the amount you would like to loan: "))
    months = int(input("Enter for how many months you would like to make a loan: "))
    margin = 0.02

    monthly_repayment = amt * (fixed_rate + margin) * (1 + fixed_rate + margin)** months / (1 + fixed_rate + margin)** months - 1
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


loan_info()