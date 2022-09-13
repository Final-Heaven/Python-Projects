
# Creating a parent class with default values
class Person:
    name = 'Unspecified'
    email = ' '
    address = ' '
    phone_number = '123-456-7890'

    # Creating a method for retrieving information about a person by entering their name
    def getInformation(self):
        name_search = input("Enter name of student or faculty: ")
        if (name_search == self.name):
            print("\nName: {}\nEmail: {}\nAddress: {}\nPhone Number: {}".format(self.name, self.email, self.address, self.phone_number))
        else:
            print("That person could not be found. Please check your entry and try again.")


# Creating a child class
class Teacher(Person):
    department = 'Unspecified'
    room_number = 999

    # Utilizing polymorphism to override parent class method and return information pertinent to teachers only
    def getInformation(self):
        name_search = input("Enter name of student or faculty: ")
        if (name_search == self.name):
            print("\nName: {}\nEmail: {}\nAddress: {}\nPhone Number: {}\nDepartment: {}\nRoom Number: {}".format(self.name, self.email, self.address, self.phone_number, self.department, self.room_number))
        else:
            print("That person could not be found. Please check your entry and try again.")


# Creating a second child class
class Student(Person):
    student_id = 12345678
    gpa = 2.00

    # Utilizing polymorphism to override parent class method and return information pertinent to students only
    def getInformation(self):
        name_search = input("Enter name of student or faculty: ")
        if (name_search == self.name):
            print("\nName: {}\nEmail: {}\nAddress: {}\nPhone Number: {}\nStudent ID: {}\nGPA: {}".format(self.name, self.email, self.address, self.phone_number, self.student_id, self.gpa))
        else:
            print("That person could not be found. Please check your entry and try again.")
