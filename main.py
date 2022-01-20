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

#Write your code below this line 

import random

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computerChoice = random.randint(0,2)

if  computerChoice == 0:
  print(rock)
  if userChoice == 1 :
    print("You Win!")
  else:
    print("You Loss!")
elif computerChoice == 1:
  print(paper)
  if userChoice == 0 :
    print("You Win!")
  else:
    print("You Loss!")
else:
  print(scissors)
  if userChoice == 1 :
    print("You Win!")
  else:
    print("You Loss!")

if computerChoice == userChoice:
  print("Draw!")
