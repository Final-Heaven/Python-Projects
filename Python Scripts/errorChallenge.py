

def getInfo():
    var1 = input("Please input the first number to be added: ")
    var2 = input("Please input the second number to be added: ")
    try:
        var3 = int(var1) + int(var2)
        print("{} + {} = {}".format(var1, var2, var3))
    except:
        print("You did not provide a valid number to be added.")
    finally:
        print("Moving on...")
    






if __name__ == "__main__":
    getInfo()
