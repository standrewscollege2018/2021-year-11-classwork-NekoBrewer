#aks for your to enter a nummber from 1-10 and if it's the coorect answer it'll say you're correct
NUM = 4
keep_asking = True
while keep_asking == True:
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

