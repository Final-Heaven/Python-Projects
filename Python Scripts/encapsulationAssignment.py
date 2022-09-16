

class ExampleProtect:
    def __init__(self):
        self._protectedVar = 10

obj = ExampleProtect()
obj._protectedVar = 20
print(obj._protectedVar)

class ExamplePrivate:
    def __init__(self):
        self.__privateVar = 15

    def get_private(self):
        print(self.__privateVar)

    def set_private(self, private):
        self.__privateVar = private

obj = ExamplePrivate()
obj.get_private()
obj.set_private(30)
obj.get_private()



