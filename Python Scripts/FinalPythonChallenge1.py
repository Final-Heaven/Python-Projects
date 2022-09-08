import time

X = 10 # Task 1
Month = "December" # Task 2
Y = 2.5 # Task 3
print(X)# Task 4
print(Month) # Task 4
print(Y) # Task 4
time.sleep(.5)

print(X+Y) # Task 5a
print(X*Y) # Task 5b
print(X/Y) # Task 5c
Z = 20 # Task 5d
print(X%Y) # Task 5e
time.sleep(.5)

print(X>5 and X<15) # Task 6a
print(X==10 or X>20) # Task 6b
print(not(X>15 or X<12)) # Task 6c
time.sleep(.5)

if Z==X: # Task 7a
    print("20 is equal to 10")
elif Z>X: # Task 7b
    print("20 is greater than 10")
else: # Task 7c
    print("20 is not equal to or greater than 10")
time.sleep(.5)

A = 1
while A<6: # Task 8
    print(A)
    A += 1
    time.sleep(.5)

for x in range(1,6): # Task 9
    print(x)
    time.sleep(.5)

mylist = ["Windows", "Linux", "Unix", "MacOS"]
for x in mylist: # Task 10
    print(x)
    time.sleep(.5)

mytuple = ("Toyota", "Chevrolet", "Honda", "Subaru", "Ford")
for x in mytuple: # Task 11
    print(x)
    time.sleep(.5)

def my_function(): # Task 12
    print("My function was correctly called")
my_function() # Task 13

















