#This program calculates movie ticket prices for different ages
age = int(input("how old are you? "))
if age < 5:
    print("Free")
elif age < 13:
    print("$7")
else:
    student = input("Are you a student? yes/no ")
    if student =="yes":
        print("$8")
    elif student =="no" and age >= 18 and < 65:
        print("$12")
    else:
        print("$9")