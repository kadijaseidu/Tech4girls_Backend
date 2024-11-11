#!/usr/bin/python3
# Question 1: Division Calculator

"""using ZeroDivisionError and ValueError to handle possible errors"""
try:
  numerator = int(input("Enter the numerator: "))
  denominator = int(input("Enter the denominator: "))
  result = numerator / denominator
except ZeroDivisionError:
   print("you can not divide by zero")
except ValueError:
   print("please enter only valid integers")
else:
   print("The result is:", result)