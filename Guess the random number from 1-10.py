#makes the number between one and 10 and you must guess it
high_score = 10000
ask_number = True
import random
NUM = random.randint(1,100)
keep_asking = True
#set the counter
counter = 0


while keep_asking == True:
    counter += 1
    ask_number = True
    while ask_number == True:
        try:
            number = int(input("Guess an integer between 1 and 100 "))
            ask_number = False
        except:
            print("That's not an integer")
    if number == NUM:
        keep_asking = False
        print("Good job you guessed the number")
    if number > NUM and number <=100:
        print("Too High Guess lower")
    if number < NUM and number >0:
        print("Too Low Guess higher")
    if number > 100 or number <=0:
        print("Invalid Number")
if counter < high_score:
    high_score = counter
    print("Congratulations you have a new record")
if counter < 2:
    print("you took", counter, "try")
elif counter >= 2:
    print("You took", counter, "try's")
