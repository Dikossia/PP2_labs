import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        try:
            guess = int(input("\nTake a guess.\n"))
            guesses += 1
            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number!")


"""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12
Your guess is too low.
Take a guess.
19
Good job, KBTU! You guessed my number in 2 guesses!
"""