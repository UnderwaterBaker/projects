import random #imports the random module

guesses = 0 #defines the guesses variable as 0

number = random.randint(1, 10) #assignes the variable 'number' a random value between 1-10
print("Im thinking of a number between 1 and 10") 

while guesses < 5: #creates a while loop that will stay until guesses is greater than 5
    print("take a guess: ")#--
    guess = input()        #  |--take user input and converts it to a interger
    guess = int(guess)     #--

    guesses = guesses + 1 #add 1 to the guesses variable and itterates back to the begenning of the whihle loop

    if guess < number: # if users guess is lower than number it will execute code below
        print("Too low my man")

    if guess > number: # if users guess is higher than number it will execute code below
        print("Too high my man")

    if guess == number: # if guess has the same value as number the loop will break
        break

if guess == number: # if your guess has the same value as numbher it will execute the code below
    guesses = str(guesses) # convers guesses variablt from intiger to string
    print("Just right my man and it only took you " + guesses + " guesses!")
