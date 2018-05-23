import random

win = False # boolean value to keep the game moving until the player wins
numberGuessed = random.randrange(0, 10001) # sets a random number between 0 and 10000 inclusive
numberOfGuesses = 1 # used to keep track of the number of guesses
guess = -1 # variable used to store the user's guess 

# this is the main loop that your game will play in
# remember that when the user has 
while not win:
    # ask the user what their guess is
    if numberOfGuesses > 0:
        try:
            guess = int(input("Guess a number between 0 and 10000: "))
        except ValueError:
            print("Please choose an integer.")
            guess = -1
    else:
        try:
            guess = int(input("Try again: "))
        except ValueError:
            print("Please choose an integer.")
            guess = -1

    difference = abs(numberGuessed - guess)
    print(difference)
    # if statement to see if their guess is correct
    if guess < 0:
        pass
    elif guess > numberGuessed:
        if difference < 50:
            print("Getting closer, but still high.")
        else:
            print("Too high.")
    else:
        if difference < 50:
            print("Getting closer, but still low.")
        else:
            print("Too low.")

# print out how that the user has won
print("You won!")
# print out how many guesses it took the user
print("It only took " + numberOfGuesses + " guesses.")