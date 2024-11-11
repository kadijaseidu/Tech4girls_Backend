#!/usr/bin/python3
# Question 5: List Index Access

"""Using IndexError and ValueError to handle possible Errors"""
items = ["apple", "banana", "cherry"]
try:
 index = int(input("Enter the index of the item you want to access: "))
 print("You selected:", items[index])
except IndexError:
  print("Error: please enter a valid index")
except ValueError:
  print("Error: Please enter a valid integer")