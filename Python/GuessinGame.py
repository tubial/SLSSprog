import random

win = False # boolean value to keep the game moving until the player wins
numberGuessed = random.randrange(0, 10001) # sets a random number between 0 and 10000 inclusive
numberOfGuesses = 0 # used to keep track of the number of guesses
guess = -1 # variable used to store the user's guess 

print(numberGuessed)

# this is the main loop that your game will play in
while not win:
    # ask the user what their guess is
    if numberOfGuesses <= 0:
        guess = input("Guess a number between 0 and 10000 (type e to exit): ")
    else:
        guess = input("Try again (type e to exit): ")

    if guess == "e":
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please choose an integer.")
        guess = -1
        numberOfGuesses -= 1

    numberOfGuesses += 1

    difference = abs(numberGuessed - guess)

    # if statement to see if their guess is correct
    if guess == numberGuessed:
        win = True
    elif guess < 0:
        pass
    elif guess > numberGuessed:
        if  difference < 100:
            print("Getting closer, but still high.")
        elif difference < 50:
            print("Closer! A little high.")
        elif difference:
            print("Too high.")
    else:
        if difference < 100:
            print("Getting closer, but still low.")
        elif difference < 50:
            print("Closer! A little low.")
        else:
            print("Too low.")

if win:
    # print out how that the user has won
    print("You won!")
    # print out how many guesses it took the user
    print("It only took " + str(numberOfGuesses) + " guesses.")