#!/usr/bin/python3

#defining two variables
x = 13
y = 9

#performing calculations between x and y
addition = x + y
subtraction = x - y 
multiplication = x * y
division = x / y
floor_division = x // y 
exponentiation = x ** y
modulus = x % y 

#using comparisms for x and y
equal_to = x == y 
not_equal = x != y 
less_than = x < y 
greater_than = x > y 
less_or_equal = x <= y 
greater_or_equal = x >= y 

#printing the results of each calculation using f-string
print(f"Addition (x + y): {addition}")
print(f"Subtraction (x - y): {subtraction}")
print(f"multiplication (x * y): {multiplication}")
print(f"division (x / y): {division}")
print(f"floor_division (x // y): {floor_division}")
print(f"exponentiation (x ** y): {exponentiation}")
print(f"modulus (x % y): {modulus}")

print(f"is x equal to y? {equal_to}")
print(f"is x not equal to y? {not_equal}")
print(f"is x less tha y? {less_than}")
print(f"is x greater than y? {greater_than}")
print(f"is x less than or equal to y? {less_or_equal}")
print(f"is x greater than or equal to y? {greater_or_equal}")