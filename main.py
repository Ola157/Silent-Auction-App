from art import logo
import os

print(logo)

def clear_screen():
    """Clears the terminal screen without stopping the program."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def find_highest_bider(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bid_list = {}
should_continue= True
while should_continue:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bid_list[name]= price
    other_bid = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    clear_screen()

    if other_bid == "no":
        should_continue = False
        find_highest_bider(bid_list)


