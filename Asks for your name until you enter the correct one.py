#start asking their namedtuple
#set Boolean to True
keep_asking = True

#start asking their name
while keep_asking == True:
    name = input("Enter your name ")
    if name == "neko" or name =="Neko":
        keep_asking = False
        print("Hi Neko")
    else:
        print("Wrong name")

#loop is now finishef, so greet henry print("hi Henry")ne