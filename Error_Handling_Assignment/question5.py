#!/usr/bin/python3
# Question 6: Age Validator

"""using ValueError to handle possible errors"""
try:
   age = int(input("Enter your age: "))
   if age < 0:
    print("Age cannot be negative!")
   elif age > 120:
    print("That age is unlikely!")
   else:
    print("Your age is:", age)
except ValueError:
  print("Please enter a valid integer")