import random

# Get level 
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate random number between 1 and level
random_number = random.randint(1, level)

# Keep guessing until correct
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess > random_number:
            print("Too large!")
        elif guess < random_number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
