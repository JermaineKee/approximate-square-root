
def newtroot():
    pass

#ask user for a positive number
num = float(input("Give me a positive number " ))
#Ask the user to guess the square root of the number...
guess = float(input("guess the square root "))

guess2 = ((num / guess) + guess) / 2
guess3 = ((num / guess2) + guess2) / 2
guess4 = ((num / guess3) + guess3) / 2
guess5 = ((num / guess4) + guess4) / 2
guess6 = ((num / guess5) + guess5) / 2




print(round(guess6, 2))
