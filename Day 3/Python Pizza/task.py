print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
# base price
if size == "S":

    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# pepperoni condition
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3

# cheese case
if extra_cheese  == "Y":
    if size == "S":
        bill += 1

        # final bill
print(f"Your final bill is: ${bill}.")