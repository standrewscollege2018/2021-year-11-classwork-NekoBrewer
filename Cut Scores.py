#This program calvulates grades
#Set up cut scores

CUT_A = 90
CUT_B = 70
CUT_C = 50

#Get the scores
#first check if the mark is between 0 and 100
mark = int(input("Enter score "))

#Calculate Grades
if mark >=0 and mark <=100:
   if mark >= CUT_A:
    print("A")
   elif mark >= CUT_B:
    print("B")
   elif mark >= CUT_C:
    print("C")
   else:
    print("Sorry you didn't make the required score")
else:
    print("invalid score")