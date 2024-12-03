from config import session
from models import Backend

class Backend_crud:
    def __init__(self, session):
        self.session = session

    def insert_student(self, first_name, last_name, age, email):
        new_student = Backend(first_name=first_name, last_name=last_name, age=age, email=email)
        session.add(new_student)
        session.commit()
        return new_student
    
    
    def get_all_students(self):
        return self.session.query(Backend).all()
    
    def get_student_by_first_name(self, first_name):
        return self.session.query(Backend).filter_by(first_name=first_name).first()
    
    def get_student_by_first(self, age):
        return self.session.query(Backend).filter_by(age=age).first()
    
    def update_student(self, student_id, first_name=None, last_name=None, age=None, email=None):
        selected_student = self.session.query(Backend).filter_by(student_id=student_id).first()
        if selected_student:
            if first_name:
                selected_student.first_name = first_name
            if last_name:
                selected_student.last_name = last_name
            if age:
                selected_student.age = age
            if email:
                selected_student.email = email
            self.session.commit()
        return selected_student
    
    def deleted_student(self, student_id):
        selected_student = self.session.query(Backend).filter_by(student_id=student_id).first()
        if selected_student:
            self.session.delete(selected_student)
        self.session.commit()
        return f'student with {student_id} has been deleted'
    

    
      
backend_crud = Backend_crud(session)

"""new_student2 = backend_crud.insert_student("Victoria", "Yimaney", 25, "victoriayimaney19@gmail.com")
print(new_student2)"""