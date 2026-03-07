print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("OMG you are at the cross road🤯! Where do you want to go? type 'left' or 'right'.").lower()
if choice1 == "right":
    print("ohoo! you entered a blackhole😵‍💫 ")
elif choice1 == "left":
   choice2 = input("you have come to a lake! now what the next move champ? type 'swim' to swim across lake or type 'boat' to wait for the boat 🧐").lower()
   if choice2 == "boat":
            choice3 = input(" you arrived island unharmed , now the final hurdle you are infront of 3 doors with colour red , blue, yellow ! which door u gonna choose 🥶")
            if choice3 == "red":
             print("you entered a room full of FIRE ! GAME OVER🥴")
            elif  choice3 == "blue":
             print("you entered a room full of BEASTS ! GAME OVER🥴")
            elif choice3 == "yellow":
             print("HURRY YOU FINALLY FOUND THE TREASURE 🤩")
            else:
             print("dont act smart choose door given above 😏")
   else:
        print("ohoo!😢 you are now a meal for angry trout")

else :
 print("what rey enter the valid input!😤")
