import datetime


x = datetime.datetime.now()

def getBranchTimes():
    PortlandHour = int(x.strftime("%H"))
    Minute = int(x.strftime("%M"))
    NewYorkHour = PortlandHour + 3
    LondonHour = PortlandHour + 8


    print("The current time in Portland is " + str(PortlandHour) + ":" + str(Minute))
    if PortlandHour >= 9 and PortlandHour < 17:
        print("The Portland branch is currently open.")
    else:
        print("The Portland branch is currently closed.")
    print("")


    print("The current time in New York is " + str(NewYorkHour) + ":" + str(Minute))
    if NewYorkHour >= 9 and NewYorkHour < 17:
        print("The New York branch is currently open.")
    else:
        print("The New York branch is currently closed.")
    print("")

    print("The current time in London is " + str(LondonHour) + ":" + str(Minute))
    if LondonHour >= 9 and LondonHour < 17:
        print("The London branch is currently open.")
    else:
        print("The London branch is currently closed.")
    print("")


if __name__ == "__main__":
    getBranchTimes()
