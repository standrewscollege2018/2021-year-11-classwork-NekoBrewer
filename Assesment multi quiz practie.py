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
"C(8848m)",
"A(Canberra)",
"D(Vietnam)",
"C(Ottawa)",
"B(Turkey)",
"D(Asia)"
]



answer1 = input(question_prompts[0])
if answer1.lower() == "c" or answer1.lower() == "8848" or answer1.lower() == "8848m":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is c.8848m")
    print("Score: ", score,"out of 6")



answer2 = input(question_prompts[1])
if answer2.lower() == "a" or answer2.lower() == "canberra":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is a.Canberra.")
    print("Score: ", score,"out of 6")



answer3 = input(question_prompts[2])
if answer3.lower == "d" or answer3.lower() == "vietnam":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is d.Vietnam.")
    print("Score: ", score,"out of 6")



answer4 = input(question_prompts[3])
if answer4.lower() == "c" or answer4.lower() == "ottawa":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is c.Ottawa.")
    print("Score: ", score,"out of 6")



answer5 = input(question_prompts[4])
if answer5.lower() == "b" or answer5.lower() == "turkey":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is b.Turkey.")
    print("Score: ", score,"out of 6")



answer6 = input(question_prompts[5])
if answer6.lower() == "d" or answer6.lower() == "asia":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is D.Asia.")
    print("Score: ", score,"out of 6")





