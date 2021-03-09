#This code will figure out a cars speed and find out how much they should be charged if they're faster than the speed limit.
below_ten = (1,9)
below_twenty = (10,19)
below_thirty = (20,29)


keep_asking = True
keep_doing = True
keep_thinking = True


print("Hello I hope you're having a good day so far")

while keep_asking == True:
    speeders_name = input("What is the speeder's name ")
    if speeders_name.lower() == "end":
        print("You have ended the code")
        keep_asking = False
    else:
        while keep_doing == True:
            try:
                speed_limit = int(input("What is the speed limit (km/h) "))
                keep_doing = False
            except:
                print("Please enter a number")
        while keep_thinking == True:
            try:
                speeders_speed = int(input("What is the speeder's speed (km/h) "))
                keep_thinking = False
            except:
                print("Please enter a number")
        if speeders_speed <= speed_limit:
            print(speeders_name, "was not travelling over the speed limit no fine is neccessary")
        else:
            if speeders_speed - speed_limit <10:
                fine = 30
            elif speeders_speed - speed_limit < 20:
                fine = 80
            elif speeders_speed - speed_limit < 30:
                fine = 130
            elif speeders_speed - speed_limit > 29:
                fine = 180
            print("A user named {} is caught doing {} in a {} zone they were going {} over the limit and will be fined ${}".format(speeders_name, speeders_speed, speed_limit, speeders_speed-speed_limit, fine))

