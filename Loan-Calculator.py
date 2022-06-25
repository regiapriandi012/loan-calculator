import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
inputan = input()
if inputan == "n":
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / (12 * 100)
    n = math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i)
    n_year = int(n // 12)
    n_month = math.ceil(n % 12)
    if n_year == 0 and n_month == 12:
        n_year += 1
        n_month %= 12
        print("It will take {} year and {} months to repay this loan!".format(n_year, n_month))
    elif n_year >= 1 and n_month == 12:
        n_year += 1
        n_month %= 12
        print("It will take {} years and {} months to repay this loan!".format(n_year, n_month))
    elif n_year > 1 and n_month > 1:
        print("It will take {} years and {} months to repay this loan!".format(n_year, n_month))
    elif n_year == 1 and n_month == 1:
        print("It will take {} year and {} month to repay this loan!".format(n_year, n_month))
    elif n_year > 1 and n_month == 1:
        print("It will take {} years and {} month to repay this loan!".format(n_year, n_month))
    elif n_year == 1 and n_month > 1:
        print("It will take {} year and {} months to repay this loan!".format(n_year, n_month))
elif inputan == "a":
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the number of periods:")
    number_of_periods = float(input())
    print("Enter the loan interest:")
    loan_interest = float(input())
    i = loan_interest / 1200
    base = 1 + i
    payment = loan_principal * (i * math.pow(base, number_of_periods)) / (math.pow(base, number_of_periods) - 1)
    print(f'Your monthly payment = {math.ceil(payment)}!')
elif inputan == "p":
    print('Enter the annuity payment:')
    annuity_payment = float(input())
    print('Enter the number of periods:')
    number_of_periods = float(input())
    print('Enter the number of periods:')
    loan_interest = float(input())
    i = loan_interest / 12 / 100
    loan_principal = annuity_payment / (
            (i * math.pow(1 + i, number_of_periods)) / (math.pow(1 + i, number_of_periods) - 1))
    print(f'Your loan principal = {math.floor(loan_principal)}!')