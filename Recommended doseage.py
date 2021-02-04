REQUIRED_AGE = 12
DOSEAGE = 10
age = int(input("How old are you "))

if age > 0:
   if age >= REQUIRED_AGE:
    print("Recommended two 500mg tablets of paracetamol")
   elif age < REQUIRED_AGE:
    weight = int(input("How much do you weigh(kg) "))
    if weight >0:
     print("Recommended doseage=", DOSEAGE*weight,"mg")
     if weight <=0:
         print("invalid weight")
else: print("Invalid age")
