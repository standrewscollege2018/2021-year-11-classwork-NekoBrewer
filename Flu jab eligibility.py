#Asks for your weight and age and determines if you're eligible for your flu shot
AGE = 18
WEIGHT = 50
YOUR_AGE = int(input("How old are you  "))
YOUR_WEIGHT = int(input("How much do you weigh  "))
if YOUR_WEIGHT > WEIGHT and YOUR_AGE >= AGE:
   print("you are eligible for your flu jab")