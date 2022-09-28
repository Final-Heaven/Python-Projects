
# Creating a parent class with default values
class Person:
    name = 'Unspecified'
    email = ' '
    address = ' '
    phone_number = '123-456-7890'


# Creating two child classes (with default values) that inherit from the parent class of "Person"
class Teacher(Person):
    department = 'Unspecified'
    room_number = 999

class Student(Person):
    student_id = 12345678
    gpa = 2.00
    
