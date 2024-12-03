from config import session
from models import Laptops  

class Laptop_crud:
    def __init__(self, session):
        self.session = session
    

    def insert_laptop(self, laptop_name, laptop_number, student_id):
        #Insert a new laptop into the database.
        new_laptop = Laptops(laptop_name=laptop_name, laptop_number=laptop_number, student_id=student_id)
        self.session.add(new_laptop)
        self.session.commit()
        return new_laptop

    def get_all_laptops(self):
        #Get all laptops from the database.
        return self.session.query(Laptops).all()

    def get_laptop_by_id(self, laptop_number):
        #Get a laptop by its unique number.
        return self.session.query(Laptops).filter_by(laptop_number=laptop_number).first()

    def get_laptop_by_name(self, laptop_name):
        #Get a laptop by its name.
        return self.session.query(Laptops).filter_by(laptop_name=laptop_name).first()

    def update_laptop(self, laptop_number, laptop_name=None, student_id=None):
        #Update an existing laptop's details.
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number=laptop_number).first()
        if selected_laptop:
            if laptop_name:
                selected_laptop.laptop_name = laptop_name
            if student_id:
                selected_laptop.student_id = student_id
            self.session.commit()
        return selected_laptop

    def delete_laptop(self, laptop_number):
        #Delete a laptop by its number.
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number=laptop_number).first()
        if selected_laptop:
            self.session.delete(selected_laptop)
            self.session.commit()
            return f"Laptop with ID {laptop_number} has been deleted"
        else:
            return f"No laptop found with ID {laptop_number}"
        


if __name__ == '__main__':
    laptop_crud = Laptop_crud(session)

    #new_laptop = laptop_crud.insert_laptop("HP Spectre x360", 2000, 8)
    #print(new_laptop)

    # Get_all_laptops
    #all_laptops = laptop_crud.get_all_laptops()
    #print(all_laptops)

    # Get a laptop by its number
    #laptop_id = laptop_crud.get_laptop_by_id(1001)
    #print(laptop_id)

    # Get a laptop by its name
    #laptop_name = laptop_crud.get_laptop_by_name("MacBook Pro")
    #print(laptop_name)

    # Update a laptop
    #updated_laptop = laptop_crud.update_laptop(2017, laptop_name="MacBook Air")
    #print(updated_laptop)

    # Delete a laptop
    #delete_laptop = laptop_crud.delete_laptop(2000)
    #print(delete_laptop)