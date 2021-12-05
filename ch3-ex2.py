#!/usr/bin/env python3
lucky = input("Please enter your lucky number:")
if not lucky.isnumeric(): # I would have guessed this would also be true for floats, etc.?
    print("not an integer!")
else:
    index = 0
    for each_digit in lucky:
        index = index + 1
    print("It's an integer, and has",index,"digit(s)")
