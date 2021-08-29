#!/usr/bin/env python3
longstring = input("Please input a string: ")
print("Does it end with a period?", longstring.endswith(".")) 
print("Is it all alphanumeric?", longstring.isalpha())
print("Does it contain the letter 'x'?", 'x' in longstring)
print("Here is all the string with every 'e' replaced by 'E':", longstring.replace("e", "E"))
