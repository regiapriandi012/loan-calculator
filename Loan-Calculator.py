import math
# write your code here
print('Enter the loan principal:')
principal = int(input())
print("What do you want to calculate?")
print("type \"m\" for number of monthly payments,\ntype \"p\" for the monthly payment:")
inputan = input()
try:
    if inputan == "m":
        print("Enter the monthly payment:")
        inputan_m = int(input())
        hasil = math.ceil(principal/inputan_m)
        if hasil == 1:
            print("It will take {} month to repay the loan".format(hasil))
        elif hasil > 1:
            print("It will take {} months to repay the loan".format(hasil))
    elif inputan == "p":
        print("Enter the number of months:")
        inputan_p = int(input())
        payment = math.ceil(principal / inputan_p)
        last_payment = principal - (inputan_p - 1) * payment
        if principal % inputan_p != 0:
            print("Your monthly payment = {} and the last payment = {}.".format(payment, last_payment))
        elif principal % inputan_p == 0:
            print("Your monthly payment = {}".format(payment))
except:
    print("Input only char m and p")
