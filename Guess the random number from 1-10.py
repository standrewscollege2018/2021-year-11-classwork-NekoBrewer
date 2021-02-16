#makes the number between one and 10 and you must guess it
high_score = 10000
import random
NUM = random.randint(1,100)
keep_asking = True
#set the counter
counter = 0
while keep_asking == True:
    counter += 1
    number = int(input("Guess a number between 1 and 100 "))
    if number == NUM:
        keep_asking = False
        print("Good job you guessed the number")
    if number > NUM and number <=100:
        print("Too High Go lower")
    if number < NUM and number >0:
        print("Too Low Go higher")
    if number > 100 or number <=0:
        print("Invalid Number")
if counter < 2:
    print("you took", counter, "try")
elif counter >= 2:
    print("You took", counter, "try's")
if counter < high_score:

    print("Congratulations you have a new record")

