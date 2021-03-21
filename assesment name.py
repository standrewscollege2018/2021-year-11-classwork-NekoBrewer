import random
keep_asking_yes_no = True
keep_asking_prediction = True
keep_asking_prediction_number = True
keep_asking_name = True
check_reserve = True
reserve_checking = True
keep_thinking = True
ask_number = True
keep_asking = True
keep_asking_prediction_loop = True
NUM = random.randint(1,100)#
high_score = 10000
ask_number = True
import random
NUM = random.randint(1,100)
keep_asking = True
#set the counter
counter = 0







while keep_asking_prediction_number == True:
    keep_asking_prediction = True
    while keep_asking_prediction == True:
        try:
            prediction = int(input("Please enter how many questions you think you will get correct out of six "))
            keep_asking_prediction = False
        except:
            print("Please enter an integer between 0 and 6")

    if prediction >= 0 and prediction <= 6:
        keep_asking_prediction_number = False
    elif prediction < 0 or prediction > 6:
        print("Please enter an integer between 0 and 6")







