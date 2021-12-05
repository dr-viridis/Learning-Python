#!/usr/bin/env python3
firstnum = input("Please enter the first number:")
secondnum = input("Please enter the second number:")

if firstnum > secondnum:
    print("The first number,",firstnum,", is greater.")
elif secondnum > firstnum:
    print("The second number,",secondnum,", is greater.")
else: #should only get here if they're equal
    print("Both numbers were",firstnum)
