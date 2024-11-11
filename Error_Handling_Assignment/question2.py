#!/usr/bin/python3
# Question 2: Dictionary Lookup

"""using keyError to handle possible errors"""
data = {"name": "Alice", "age": 25, "country": "Wonderland"}
key = input("Enter the key you want to look up: ")
try:
 print("Value:", data[key])
except KeyError:
 print("please enter a valid key in the dictionary")