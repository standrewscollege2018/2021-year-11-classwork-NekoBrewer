#

step_num = 1
for num in range(0,16, step_num):
    print(num)
    if num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")