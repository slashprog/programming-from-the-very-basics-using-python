import random

number = random.randint(10, 20)
guess = 0
num_tries = 0

cancelled = False

while guess != number:
    guess = int(input("Guess a number between 10 to 20 (or 0 to exit): "))
    if guess == 0:
        print("Thank you!")
        cancelled = True
        break

    if guess < 10 or guess > 20:
        print("Number must between 10 and 20")
    elif guess < number:
        print("Try a larger number...")
    elif guess > number:
        print("Try a smaller number...")
    num_tries += 1

if not cancelled:
    print("You guessed it right in", num_tries, "tries")

