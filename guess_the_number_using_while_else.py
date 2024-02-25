import random

number = random.randint(10, 20)
guess = 0
num_tries = 0

while guess != number:
    guess = int(input("Guess a number between 10 to 20 (or 0 to exit): "))
    if not guess:
        print("Thank you!")
        break

    num_tries += 1

    if guess < 10 or guess > 20:
        print("Number must between 10 and 20")
    elif guess < number:
        print("Try a larger number...")
    elif guess > number:
        print("Try a smaller number...")
else: # DO NOT re-indent! Read up on while...else... in python tutorial
    print("You guessed it right in", num_tries, "tries")

