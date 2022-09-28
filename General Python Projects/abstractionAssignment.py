# Importing required module
from abc import ABC, abstractmethod


# Creating parent class
class birthday(ABC):
    def message(self, age):
        print("Happy {}th Birthday!".format(age)) # Prints message with given age

    # This is the abstract method. The implementation is defined in the child class below.
    @abstractmethod
    def statement(self, age):
        pass


# Creating child class
class birthday_statement(birthday):
    def statement(self, age): # This is the actual implementation of the abstract method from above
        print("I can't believe you're already {} years old!".format(age))


obj = birthday_statement() # Creating object
obj.message(25) # Passing in arguments for both methods
obj.statement(25)
