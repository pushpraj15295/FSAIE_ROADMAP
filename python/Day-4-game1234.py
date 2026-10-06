# random number game 

import random

random_number = random.randint(1,100)
total_guesses = 1

guess = int(input("Guess a number between 1 and 100: "))

while guess != random_number:
    if guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
    total_guesses += 1 

print(f"Congratulations! You guessed the number {random_number} in {total_guesses} guesses.")