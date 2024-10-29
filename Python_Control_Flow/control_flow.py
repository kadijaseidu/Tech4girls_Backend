#!/usr/bin/python3
"""asking the user for their age and running the If-Else command"""
age = int(input("what is your age"))
if age < 18:
    print("you are a minor.")
elif 18 <= age < 65:
    print("you are an adult")
else:
    print("you are a senior")