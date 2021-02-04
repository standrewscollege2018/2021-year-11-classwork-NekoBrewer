REQUIRED_AGE = 12
DOSEAGE = 10
AGE = int(input("How old are you "))


if AGE >= REQUIRED_AGE:
   print("Recommended two 500mg tablets of paracetamol")
elif AGE < REQUIRED_AGE:
    WEIGHT = int(input("How much do you weigh(kg) "))
    print("Recommended doseage=", DOSEAGE*WEIGHT,"mg")

