#!/usr/bin/python3
# Question 3: Integer Conversion

"""using the try-except block to catch valueError in Error handling"""
user_input = input("Enter a number: ")
try:
 converted_number = int(user_input)
except ValueError:
 print("Error: Please enter a valid integer")
else:
 print("The number you entered is:", converted_number)