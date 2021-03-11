#This code asks what the auction
keep_thinking = True
keep_asking = True
highest_bid = 0
get_item = True
get_name = True
bid_checking = True
reserve_checking = True
while get_item == True:
    Auction_Item = input("What is the item being auctioned? ")
    if Auction_Item.replace(" ", "") == "":
        print("Please enter an item")
    else:
        get_item = False

check_reserve = True
while check_reserve == True:
    try:
        reserve_price = int(input("What is the reserve price($)? "))
        check_reserve = False
    except:
        print("Enter an integer")
while keep_thinking == True:
    if reserve_price < 0:

        while reserve_checking == True:
            try:
                reserve_price = int(input("Please enter a higher reserve price ($) "))
                reserve_checking = False
            except:
                print("Please enter an integer")
    if reserve_price >= 0:
        highest_bid = reserve_price
        keep_thinking = False
print("The auction for the", Auction_Item, "has started")
print("The reserve price is $", highest_bid)

while keep_asking == True:

    while get_name == True:
        name = input("What is your first name? ")
        if name.replace(" ","") == "":
            print("Please enter a valid name? ")
        elif name == "end":
            keep_asking = False
            break
        else:




            while bid_checking == True:
                try:
                    bid = int(input("what is your bid?($) "))
                    if bid <= -1:
                        print("Enter a postive number")
                    elif bid < reserve_price or bid < highest_bid:
                        print("Please enter a higher bid")
                        bid_checking = False

                    else:
                        highest_bid = bid
                        print("Highest bid so far is",name,"with $",highest_bid)
                        bid_checking = False
                except:
                    print("Please enter an integer")
            get_name = True
            bid_checking = True

print("The auction for the", Auction_Item, "finished with a bid of $",highest_bid, "from", name)