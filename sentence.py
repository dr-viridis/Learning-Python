#!/usr/bin/env python3
sentence = input("Please type in a sentence: ")
first_char = sentence[0]
last_char = sentence[-1]
print("First char is", first_char, "and it appears", sentence.count(first_char), "times in the sentence") 
print("Last char is", last_char, "and it appears",  sentence.count(last_char), "times in the sentence") 
