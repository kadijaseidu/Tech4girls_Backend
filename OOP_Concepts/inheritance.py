#!/usr/bin/python3
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        """Display employee details"""
        return f"Information of Employee: \nName: {self.name} \nPosition: {self.position}" 

"""Create an instance of employee and calling get_details() method"""
employee = Employee("Gifty", "Communications Officer")
print(employee.get_details())


"""Define the child class Manager that inherits from Employee"""
class Manager(Employee):
    def __init__(self, name, position, department):
        
        """Use super() to initialize inherited attributes"""
        super().__init__(name, position,)
        self.department = department
        
    def get_details(self):
        """Override the method to include department details"""
        return f"Information of Manager: \nName: {self.name} \nPosition: {self.position} \nDepartment: {self.department}."
    

"""Create an instance of manager and calling get_details() method"""
manager = Manager("Gideon", "Senior Manager", "Marketing")
print(manager.get_details())