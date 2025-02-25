
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random
def randDice():

    # Write your logic to generate 2 numbers between 1 and 6 here
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Sum 2 numbers
    sum = die1 +die2
    # return sum to calling function
    return sum
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def __main__():
    total = 0
    for i in range(100):
        total += randDice()
        print(total/100)
__main__()
#ethan collins 2/25/2025 average dice