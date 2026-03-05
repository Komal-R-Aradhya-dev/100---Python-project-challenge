print("welcome to the tip calculator")
bill = float(input("what was your total bill\n"))
tip =  int(input("how much tip would u like to give? 10,12 or 15\n"))
people = int(input("how many people will u split the bill between?\n"))
tip_amount = bill * (tip/100)
final = (bill + tip_amount)/people
rup = ("₹" )
print("each person should pay: " + rup + str(final))