#makes the number between one and 10 and you must guess it
import random
NUM = random.randint(1,10)
keep_asking = True
#set the counter
counter = 0
while keep_asking == True:
    counter += 1
    number = int(input("Guess a number between 1 and 10 "))
    if number == NUM:
        keep_asking = False
        print("Good job you guessed the number")
    if number > NUM and number <=10:
        print("Go lower")
    if number < NUM and number >0:
        print("Go higher")
    if number > 10 or number <=0:
        print("Invalid Number")
print("You took", counter, "tries")
