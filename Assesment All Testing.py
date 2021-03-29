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






'''The question is asked along with the answer options and you enter your answer and if it's correct
your score goes up by one and it tells you how many questions you've got correct out of the amount answered.
But if you get the question wrong it will tell you that you got it wrong and the possible answers that you
could have entered as well as your score and if you jsut click enter or the space bar however many time
and then enter it will tell you to enter an answer'''
for i in range(len(question_prompts)):
    keep_asking_for_loop = True
    while keep_asking_for_loop == True:
        question = input(question_prompts[i])
        if question.replace (" ","") == "":
            print("Please enter an answer")
        else:
            keep_asking_for_loop = False
    questions_asked += 1
    if question.lower() in answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The possible answers are", answers[i])
    print("Score = {} out of {}".format(score,questions_asked))









