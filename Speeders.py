#This code will figure out a cars speed and find out how much they should be charged if they're faster than the speed limit.
keep_asking = True


print("Hello I hope you're having a good day so far")

while keep_asking == True:
    speeders_name = input("What is the speeder's name ")
    if speeders_name == end or speeders_name == End:
        print("You have ended the code")
        keep_asking = False
    speed_limit = int(input("What is the speed limit (km/h) "))
    speeders_speed = int(input("What is the speeder's speed (km/h) "))
    print("A user named () is caught doing () in a () zone they were going ()-()over the limit and will be fined dollars")


