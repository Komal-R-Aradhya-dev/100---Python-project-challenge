import art
print (art.logo)
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in
def compare_it(bidder):
    high_amount = 0
    winner = ""
    for name in bidder:
        amount = bidder[name]
        if amount > high_amount:
            high_amount = amount
            winner = name
    print( {f"The winner is {winner} with a bid of ₹{high_amount}."})

bid = {}
continue_bidding = True
while continue_bidding:

    name = input("What is your name?")
    price = int(input("What is your bid? : ₹"))
    bid[name] = price
    should_continue = input("Would you like to continue? \"yes\" or \"no\" ").lower()
    if should_continue == "no":
        continue_bidding = False
        compare_it(bid)
    elif should_continue == "yes":
        continue_bidding = True
        print(" \n  "* 20 )