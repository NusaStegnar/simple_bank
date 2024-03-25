
def get_loan_monthly_repayment(amt, months, interest):
    monthly_rate = interest/12
    monthly_repayment = amt*((monthly_rate*((monthly_rate + 1)**months)/(((monthly_rate + 1)**months) - 1)))
    return round(monthly_repayment)


print(get_loan_monthly_repayment(50000, 48, 0.06))