#Lecture 22
#K-electric project using binary system (1 and 0) as input in python

number = int(input("Enter a number: "))

if number == 1:
    print("Electricity is coming from K-Electric")
elif number == 0:
    print("Loadshedding! use UPS...")
else:
    print("Invalid input")