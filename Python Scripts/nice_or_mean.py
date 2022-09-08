# Python:  3.10.6
#
# Author:  Daniel Castillo
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#          Demonstrating how to pass variables from function to function while producing a functional game.
#          Remember, function_name(variable) means that we pass in the variable.
#          return variable means that we are returning the variable back to the calling function.


def start():
    print("Hello {}!".format(get_name()))


def get_name():
    name = input("What is your name? ")
    return name







if __name__ == "__main__":
    start()
