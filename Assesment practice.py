
score = 0

question_prompts = [
"Question 1! How high is Mount Everest? \na.(1550m) \nb.(2900m) \nc.(8848m) \nd.(25600m) \nAnswer: ",
"Question 2! Which if these cities isn't located in New Zealand? \na.(Canberra) \nb.(Wellington) \nc.(Queenstown) \nd.(Auckland) \nAnswer: ",
"Question 3! Hanoi is the capital of which country? \na.(Cambodia) \nb.(Laos) \nc.Thailand) \nd.(Vietnam) \nAnswer: ",
"Question 4! What is the capital of Canada? \na.(Toronto) \nb.(Vacouver) \nc.(Ottawa) \nd.(Halifax) \nAnswer: ",
"Question 5! Which of these countries isn't landlocked? \na.(Nepal) \nb.(Turkey) \nc.(Armenia) \nd.(Austria) \nAnswer: ",
"Question 6! What is the largest continent in the world? \na.(Africa) \nb.(Europe) \nc.(Antartica) \nd.(Asia) \nAnswer: "
]




answers = [
"c, 8848m, 8848)",
"a, canberra)",
"d, vietnam)",
"c, ottawa)",
"b, turkey)",
"d, asia)"
]

answer_numbers = [
"answer1",
"answer2",
"answer3",
"answer4",
"answer5",
"answer6"
]





for i in range(0,1):
    answer_numbers[0] = input(question_prompts[0])
if answer_numbers[0].lower() == answers[0]:
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is", answers[0])
    print("Score: ", score,"out of 6")