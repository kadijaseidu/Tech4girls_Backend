from config import session
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Backend(Base):
    __tablename__ = 'backend_class'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
    laptops = relationship("Laptops", back_populates="student")

    def __str__(self):
        return f"Student' ID: {self.student_id}, First_name: {self.first_name} {self.last_name}"
    
class Laptops(Base):
    __tablename__ = 'laptops'
    laptop_name = Column(String(50), unique=True)
    laptop_number = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('backend_class.student_id'), nullable=False)

    student = relationship("Backend", back_populates="laptops")

    def __str__(self):
        return f"Laptop {self.laptop_name} (ID: {self.student_id}), Number: {self.laptop_number}"



if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Tables Created')
    except Exception as e:
        print(f'an error occured: {e}')