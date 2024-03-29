import random

# Get the level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Set random number
random_number = random.randint(1, level)

# Get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            print("Too small!")  # Print "Too small!" for guesses below specified range
    except ValueError:
        pass

