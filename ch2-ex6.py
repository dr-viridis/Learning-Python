#!/usr/bin/env python3
num1 = input("Please enter the first integer:")
num2 = input("Please enter the second integer:")
print("The product of the two numbers is", (int(num1)*int(num2)))
# Casts to integer, entering "2.0" (for example) causes an error
# "ValueError: invalid literal for int() with base 10: '2.0'"
# and if you enter a non-numeric value (e.g., "a"), you get the error:
# "ValueError: invalid literal for int() with base 10: 'a'"
