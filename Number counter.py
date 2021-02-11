
#this code will ask for you to enter a starting number a stopping number and a step number and then count up to your stopping number
delay = 1
start_num = int(input("please enter a starting number "))
stop_num = int(input("please enter a stopping number "))
step_num = int(input("Change each time "))
for num in range(start_num, stop_num, step_num):
    print(num)


