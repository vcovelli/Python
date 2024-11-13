import random

def roll_dice():
    return random.randint(1,6) # Generates a random integer between 1 and 6

# Simulate a dice roll and print the result
print("You rolled a:", roll_dice())