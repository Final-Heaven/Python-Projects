import time
Name = input('Name: ')
print("Hello " + Name + "! We are going to find out how long you have been alive!")
Age = int(input("What is your age? "))
print("You are " + str(Age) + " years old.")
Months = Age*12
Days = Age*365
print(Name + " has been alive for about: " + str(Months) + " months or " + str(Days) + " days!")
time.sleep(.5)
Minutes = Age*525948
Seconds = Age*31556926
print("That would be " + str(Minutes) + " minutes, or " + str(Seconds) + " seconds!")

