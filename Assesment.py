#Geography quiz by Neko Brewer
#This quiz will have a mixture of multiple choice questions and word arnswers and will test general knowledge
score = 0
keep_asking_yes_no = True
keep_asking_prediction = True
keep_asking_prediction_number = True
keep_asking_name = True

#This is a list of the six questions that will be asked along with the answer options
question_prompts = [
"Question 1! How high is Mount Everest? \na.(1550m) \nb.(2900m) \nc.(8848m) \nd.(25600m) \nAnswer: ",
"Question 2! Which if these cities isn't located in New Zealand? \na.(Canberra) \nb.(Wellington) \nc.(Queenstown) \nd.(Auckland) \nAnswer: ",
"Question 3! Hanoi is the capital of which country? \na.(Cambodia) \nb.(Laos) \nc.(Thailand) \nd.(Vietnam) \nAnswer: ",
"Question 4! What is the capital of Canada? \na.(Toronto) \nb.(Vacouver) \nc.(Ottawa) \nd.(Halifax) \nAnswer: ",
"Question 5! Which of these countries isn't landlocked? \na.(Nepal) \nb.(Turkey) \nc.(Armenia) \nd.(Austria) \nAnswer: ",
"Question 6! What is the largest continent in the world? \na.(Africa) \nb.(Europe) \nc.(Antartica) \nd.(Asia) \nAnswer: "
]

answers = [
["c", "8848m", "8848", "8.848km"],
["a", "canberra"],
["d", "vietnam"],
["c", "ottawa"],
["b", "turkey"],
["d", "asia"]
]



print("This will be a quiz on your general knowledge of the world you live in.")

#Asks the user for their name
while keep_asking_name == True:
    name = input("Please enter your name ")
    if name.replace(" ", "") == "":
        print("Please enter a valid name")
    else:
        keep_asking_name = False


print("Welcome {}".format(name))

print("There will be 6 multi answer questions in this quiz")

#Asks the user to predict how many questions they think they'll get correct
while keep_asking_prediction_number == True:
    try:
        prediction = int(input("Please enter how many questions you think you will get correct out of six: "))
        if prediction >= 0 and prediction <= 6:
            keep_asking_prediction_number = False
    except:
        print("Please enter an integer between 0 and 6")



#Asks wether the user is ready to begin the quiz or not
while keep_asking_yes_no == True:
    yes_no = input("The quiz is ready for you please enter whether you're ready to begin or not ")
    if yes_no.lower() == "no":
        print("Please enter yes when you're ready to begin")
    elif yes_no.lower() == "yes":
        keep_asking_yes_no = False
    else:
        print("Please enter yes or no")



#This is where the code asks the user the six questions and also adds the score if you get a question correct
answer1 = input(question_prompts[0])
if answer1.lower() == "c" or answer1.lower() == "8848" or answer1.lower() == "8848m":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 1")
else:
    print("Incorrenct! The answer is c.8848m")
    print("Score: ", score,"out of 1")



answer2 = input(question_prompts[1])
if answer2.lower() == "a" or answer2.lower() == "canberra":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 2")
else:
    print("Incorrenct! The answer is a.Canberra")
    print("Score: ", score,"out of 2")



answer3 = input(question_prompts[2])
if answer3.lower == "d" or answer3.lower() == "vietnam":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 3")
else:
    print("Incorrenct! The answer is d.Vietnam")
    print("Score: ", score,"out of 3")



answer4 = input(question_prompts[3])
if answer4.lower() == "c" or answer4.lower() == "ottawa":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 4")
else:
    print("Incorrenct! The answer is c.Ottawa")
    print("Score: ", score,"out of 4")



answer5 = input(question_prompts[4])
if answer5.lower() == "b" or answer5.lower() == "turkey":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 5")
else:
    print("Incorrenct! The answer is b.Turkey")
    print("Score: ", score,"out of 5")



answer6 = input(question_prompts[5])
if answer6.lower() == "d" or answer6.lower() == "asia":
    score += 1
    print("Correct!")
    print("Score:",score,"out of 6")
else:
    print("Incorrenct! The answer is D.Asia")
    print("Score: ", score,"out of 6")



for i in range(len(question_prompts)):
    question = input(question_prompts[i])
    if question.lower() == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The possible answers are", answers[i])

#This is the end of the code where the total score will be calculated
#The code will also say if they got more, less or the same amount of questions they thought they would get correct

print("Congratulations! You have finished the quiz")
print("You predicted that you would get", prediction, "questions correct out of 6 and your final score was",score,"out of 6")
if score == prediction:
    print("Good job! your prediction was correct")
elif score < prediction:
    print("Your final score was less than you predicted better luck next time")
elif score > prediction:
    print("Amazing! your score was better than you predicted, good job")