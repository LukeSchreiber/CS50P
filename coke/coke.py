cost = 50

while cost > 0:
    print("Heres how much is still due", cost)

    coin_input = int(input("Enter a number for the coin you want to put in: "))

    if coin_input in [5, 10, 25]:
        cost -= coin_input
    else:
        print("Please enter a valid coin number")

