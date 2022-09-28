# Creating class
class ExampleProtect:
    def __init__(self):
        self._protectedVar = 10 # Initializing protected variable with value of 10


obj = ExampleProtect() # Creating object
obj._protectedVar = 20 # Setting protected variable to new value of 20
print(obj._protectedVar)


# Creating class
class ExamplePrivate:
    def __init__(self):
        self.__privateVar = 15 # Initializing private variable with value of 15

    def get_private(self): # Function to print the privateVar
        print(self.__privateVar)

    def set_private(self, private): # Function to set value of privateVar
        self.__privateVar = private


obj = ExamplePrivate() # Creating object
obj.get_private()
obj.set_private(30) # Setting privateVar to new value and then printing it
obj.get_private()



