import random

guesses = 0

number = random.randint(1, 10)
print("Im thinking of a number between 1 and 10")

while guesses < 5:
    print("take a guess: ")
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < number:
        print("Too low my man")

    if guess > number:
        print("Too high my man")

    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("Just right my man and it only took you " + guesses + " guesses!")
