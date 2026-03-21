import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image= [rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors \n "))
print("you chose:")
if user_choice <0 or user_choice >3:
    print("invalid input u loose!")
else :
    print(image[user_choice])

comp_choice= random.randint(0,2)
print("computer chose:")
print(image[comp_choice])

if user_choice == 1 and comp_choice == 2:
    print("You lose!")
elif user_choice ==0 and comp_choice ==2:
    print("you win!")
elif user_choice ==2 and comp_choice ==0:
    print("you lose!")
elif user_choice > comp_choice:
    print("you win!")
elif user_choice == comp_choice:
    print("it's a tie!")


