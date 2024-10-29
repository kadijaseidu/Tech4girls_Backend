#!/usr/bin/python3
#looping through numbers from 1 to 50. using the for loop 
for number in range(1, 51): 
    
#checking number divisibility using Elif
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)