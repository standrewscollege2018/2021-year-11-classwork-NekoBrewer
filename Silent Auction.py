#This code asks what the auction
keep_asking = True
highest_bid = 0
Auction_Item = input("What is the item being auctioned? ")
reserve_price = int(input("What is the reserve price($)? "))
print("The auction for the", Auction_Item, "has started")
while keep_asking == True:
    name = input("What is your name? ")
    bid = int(input("what is your bid?($) "))
    if bid > highest_bid:
        bid = highest_bid
    if bid < reserve_price or bid < highest_bid:
        print("Please enter a higher price")
    print("Highest bid so far is",name,"with",highest_bid)
    if bid <= -1:
        keep_asking = False
print("The auction for the", Auction_Item, "finished at", highest_bid)
