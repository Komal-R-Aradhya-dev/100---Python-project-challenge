# --print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
print("Welcome to rollercoaster, please find u r eligibility to enjoy the ride!!")
height = int(input("Enter your height in cm: \n"))
age = int(input("enter your age for ticket price: \n"))
photo = input("do u want photo ? type y for yes and n for photo ")
bill = 0
if height >= 120:
    print("You r eligible to take a worlds best ride")
    if age <= 12:
     bill = 0
     print('you have to pay ₹0 :)')
    elif age > 12 and age <= 50:
     bill = 200
     print(" PAY ₹200 only for enjoying the worlds best ride")
    elif age>50:
     bill = 150
     print("congrats senior citizen discount valid pay ₹150 only")
    if photo == "y":
        bill = bill + 15

    print ("your final bill is: ₹",bill)
else:
    print("Sorry can't ride this time please grow taller jeevan :)")