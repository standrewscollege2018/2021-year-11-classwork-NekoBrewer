
score = 0
keep_asking_yes_no = True
keep_asking_prediction = True
keep_asking_prediction_number = True
keep_asking_name = True


question_prompts = [
"Question 1! How high is Mount Everest? \na.(1550m) \nb.(2900m) \nc.(8848m) \nd.(25600m) \nAnswer: ",
"Question 2! Which if these cities isn't located in New Zealand? \na.(Canberra) \nb.(Wellington) \nc.(Queenstown) \nd.(Auckland) \nAnswer: ",
"Question 3! Hanoi is the capital of which country? \na.(Cambodia) \nb.(Laos) \nc.(Thailand) \nd.(Vietnam) \nAnswer: ",
"Question 4! What is the capital of Canada? \na.(Toronto) \nb.(Vacouver) \nc.(Ottawa) \nd.(Halifax) \nAnswer: ",
"Question 5! Which of these countries isn't landlocked? \na.(Nepal) \nb.(Turkey) \nc.(Armenia) \nd.(Austria) \nAnswer: ",
"Question 6! What is the largest continent in the world? \na.(Africa) \nb.(Europe) \nc.(Antartica) \nd.(Asia) \nAnswer: "
]


answers = [
["c, 8848m, 8848)"],
["a, canberra)"],
["d, vietnam)"],
["c, ottawa)"],
["b, turkey)"],
["d, asia)"]
]


for i in range(len(question_prompts)):
    if question_prompts.lower() == answers[i]:
        print("Correct!")
        score +=1
    else:
        question = input(question_promts[i])
        if question.lower() == question_prompts[i]
        print("Incorrect! The answer is", answers[i])





