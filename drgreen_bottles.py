#!/usr/bin/env python3

#    Your code should be well-formatted and have descriptive variable/function names.
#    Your code should have comments to increase code readability. You at least should explain what any function you have does with comments. No comments in the code will result in a loss of points.
#    Your code should TAKE COMMAND LINE ARGUMENTS AND NOT USER INPUT. Using user input will result in a significant loss of points!
#    In chapter 6, there is information about how to use the sys module to take command line arguments.
#    You should be able to run python3 username_bottles.py from the virtual command line (replace username with your username).
#    It should output starting from the 99 bottles count.
#    Make sure that the last two bottles print "1 bottle" and then "No more bottles" instead of 1 bottle and 0 bottles.
#    If you run python3 username_bottles.py 10 (or any other number) the program should start with the specified number of bottles and go back down to no bottles.
#    Your program should handle unusual command line arguments like python3 username_bottles.py randomtext and python3 username_bottles.py -100
#    It is up to you if you want to default back to 99, exit without doing anything, or print out that the commands that are invalid.
#    Your code crashing due to unusual arguments is detrimental and will drop your score.


input_bottles = "99" # default number of bottles to be printed; string
# "bottles" will be the integer generated from input_bottles

# User input for testing, remember it will only accept command-line in 
# the submitted version

# need -h for instructions
# isnumeric to check input

input_bottles = input("Please input the number of bottles; default is 99: ")

if not input_bottles.isnumeric():
    print("Sorry, you need to give me a (nonnegative) integer number of bottles.")
    exit()

bottles = int(input_bottles)

if (bottles == 0):
    print("Not very interesting, but here goes:")
    print("No bottles of beer on the wall!")
    print("No bottles of beer!")
    print("Can't take one down")
    print("Or pass it around")
    print("Because there are no bottles of beer on the wall!\n")
    exit()

while bottles > 1:
    print(bottles, "bottles of beer on the wall!")
    print(bottles, "bottles of beer!")
    print("Take one down")
    print("And pass it around")
    bottles -= 1 
    if bottles == 1:
        print(bottles, "bottle of beer on the wall!\n")
    else: #also not very elegant, sorry
        print(bottles, "bottles of beer on the wall!\n")

# This is probably not the most elegant way to do this
# I'm sure a "real" programmer would have something slicker
# ...but should fall through to here as we decrement to 1, or if
# 1 is the starting number we're given

if bottles == 1:
    print(bottles, "bottle of beer on the wall!")
    print(bottles, "bottle of beer!")
    print("Take one down")
    print("And pass it around")
    print("No more bottles of beer on the wall!")
