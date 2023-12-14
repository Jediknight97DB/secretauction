from art import logo
import os
clear = lambda: os.system("cls")
bidders = []
item_names = ["1.Samsung 42inch TV ","2.Playstaion 5 ","3.Xbox Series X ","4.Samsung Projector ","5.JBL Home Cinema System"]
items = {1: {},2: {},3: {},4: {},5: {}}

def highest_bidder(bids):
    highest = 0
    result = ""
    for bidder in bids:
        if bids[bidder] > highest:
            highest = bids[bidder]
            result = bidder
    return result




print(logo)
print("\nWelcome to the secret auction program.")
print(f"{''.join(item_names)}")
choice = int(input("Type the number of the item you wish to bid on: "))
want_to_bid = True
exitprogram = False
while not exitprogram:
    while want_to_bid:
    
        name = input("What is your name?: ")
        bid = int(input("What's your bid? $"))
        items[choice][name] = bid
        answer = input("Are there any other bidders?(Y/N)").lower()
        if answer == "y":
            clear()
        else:
            clear()
            winner = highest_bidder(items[choice])
            print(f"The winner of item {item_names[choice-1]}is {winner}")
            want_to_bid = False
    qqq = input("Press enter to exit the program: ")
    exitprogram = True