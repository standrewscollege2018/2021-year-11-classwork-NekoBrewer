#enter three different names and then say hello to all three people
name = int(input("how many names to you want to enter "))
for i in range(0,name):
    name = input("please enter a name ")
    print("hello", name)