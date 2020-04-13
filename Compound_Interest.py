initial_amount = float(input("What is the amount of money you wish to deposit in dollars? "))
for year_number in range(1, 4):
    interest = initial_amount * 0.04
    new_balance = initial_amount + interest
    print("After {} years, your new balance is {} dollars.".format(year_number, new_balance))
    initial_amount = new_balance
