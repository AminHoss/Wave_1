cents = int(input("Please enter the number of cents you have: "))
coin_denominations = []
for coin_denomination in [200, 100, 25, 10, 5]:
    coins = (cents - (cents % coin_denomination)) / coin_denomination
    coin_denominations.append(coins)
    cents =  cents % coin_denomination
print("You have {} toonies, {} loonies. {} quarters, {} dimes, {} nickels, and {} pennies".format(coin_denominations[0], coin_denominations[1], coin_denominations[2], coin_denominations[3], coin_denominations[4], cents))
