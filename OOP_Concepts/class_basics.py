#!/usr/bin/python3
class Car:
    """modeling a class for a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        """displays and print the car's details"""
        print(f"Information of the car:\nCar Make: {self.make} \nCar Model: {self.model} \nCar Year:{self.year} ")

"""create an instance of the car class"""
my_car = Car('Nissan', 'Sentra', 2022)

"""calling the display_info() method"""
my_car.display_info()