#!/usr/bin/python3
"""defining different elements in a tuple"""
my_tuples = (5, "car", "Alice", 2.23, "orange")

"""using indexing to find the first element"""
index = my_tuples[0]
print(index)

"""using indexing to find the last element"""
index = my_tuples[-1]
print(index)

"""demostrating the use of the count() method on a tuple"""
count = my_tuples.count('car')
print(count)

"""demostrating the use of the index() method on a tuple"""
print(my_tuples.index('orange'))

"""converting an integer to a float"""
my_interger = 5
float = float(my_interger)
print(float)

"""converting a float to an integer"""
my_float = 2.23
integer = int(my_float)
print(integer)

"""a string representing a number to an integer"""
my_string_number = "4"
interger_number = int(my_string_number)
print(interger_number)

"""joining a list of strings into a single string"""
my_string_list = ["I", "love", "to", "read", "novels"]
joined_lists = " ".join(my_string_list)
print(joined_lists)