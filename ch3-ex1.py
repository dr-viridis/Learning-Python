#!/usr/bin/env python3
lucky = input("Please enter your lucky number:")
if not lucky.isnumeric(): # I would have guessed this would also be true for floats, etc.?
    print("not an integer!")
