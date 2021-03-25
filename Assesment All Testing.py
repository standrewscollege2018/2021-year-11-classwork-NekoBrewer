question_prompts = [
"Question 1: How high is Mount Everest? \na.(1550m) \nb.(2900m) \nc.(8848m) \nd.(25600m) \nAnswer: ",
"Question 2: Which if these cities isn't located in New Zealand? \na.(Canberra) \nb.(Wellington) \nc.(Queenstown) \nd.(Auckland) \nAnswer: ",
"Question 3: Hanoi is the capital of which country? \na.(Cambodia) \nb.(Laos) \nc.(Thailand) \nd.(Vietnam) \nAnswer: ",
"Question 4: What is the capital of Canada? \na.(Toronto) \nb.(Vacouver) \nc.(Ottawa) \nd.(Halifax) \nAnswer: ",
"Question 5: Which of these countries isn't landlocked? \na.(Nepal) \nb.(Turkey) \nc.(Armenia) \nd.(Austria) \nAnswer: ",
"Question 6: What is the largest continent in the world? \na.(Africa) \nb.(Europe) \nc.(Antartica) \nd.(Asia) \nAnswer: "
]


'''#These are the possible answers that will be marked as correct if entered by the user when on the
the specified question'''
answers = [
['c', '8848m', '8848', '8.848km'],
['a', 'canberra','canbera', 'canber', 'canberaa', 'canbeera'],
['d', 'vietnam', 'veitnam', 'vietname', 'veitname'],
['c', 'ottawa', 'otawa','otaawa'],
['b', 'turkey', 'turke','turky','turki','turkiy'],
['d', 'asia', 'aisa','asiaa'],
]

'''For each question they get correct the score will go up by one so they know how many they
got right at the end'''
score = 0
'''Each time another question is asked the questions asked will go up by one so that after they answer
they will know how many question they've got correct by the score and how many that has been out of by
the questions asked'''
questions_asked = 0
keep_asking_name = True
keep_asking_prediction_number = True
keep_asking_yes_no = True
keep_asking_for_loop = True






'''Asks the user to predict how many questions they think they'll get correct but will ask for an
integer between 0 and 6 if they enter a number below zero, above 6, a decimal or string'''
while keep_asking_prediction_number == True:
    try:
        prediction = int(input("Please enter how many questions you think you will get correct out of six: "))
        if prediction >= 0 and prediction <= 6:
            keep_asking_prediction_number = False
        else:
            print("Please enter an integer between 0 and 6")
    except:
        print("Please enter an integer between 0 and 6")









