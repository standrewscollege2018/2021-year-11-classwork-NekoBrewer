# Example of try and except
keep_asking = True
while keep_asking == True:
    try:
        number = int(input("please enter number "))
        print("You chose", number)
        print("**** All done****")
        keep_asking = False
    except:
        print("That's not an integer!")

