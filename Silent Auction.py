#This code asks what the auction
keep_thinking = True
keep_asking = True
highest_bid = 0
Auction_Item = input("What is the item being auctioned? ")


check_reserve = True
while check_reserve == True:
    try:
        reserve_price = int(input("What is the reserve price($)? "))
        check_reserve = False
    except:
        print("Enter an integer")
while keep_thinking == True:
    if reserve_price < 0:
        reserve_checking = True
        while reserve_ckecking == True:
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
    name = input("What is your name? ")
    bid_checking = True
    while bid_checking == True:
        try:
            bid = int(input("what is your bid?($) "))
            bid_checking = False
        except:
            print("Please enter an integer")
    if bid < reserve_price or bid < highest_bid:
        print("Please enter a higher price")
    if bid > highest_bid:
        highest_bid = bid
        print("Highest bid so far is",name,"with $",highest_bid)
    if bid <= -1:
        keep_asking = False
print("The auction for the", Auction_Item, "finished with a bid of $",highest_bid)