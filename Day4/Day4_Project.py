# ========================================================================= #
#               Day 4 Project Rock, Paper or Scissors Game                  #
# ========================================================================= #

# We're going to make a rock, paper, scissors game.
# We're going to get input from users and compare their input to the computer's choice and our program is going to decide who is gonna win.
# We're going to write our program according to The Rock, Paper, Scissors Association.
# - e.g. if user and the computer chose the same then the output will be It's a draw.
# - e.g. if user chose paper & the computer chose scissors then output will be You lose!.

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

#my first solution to this problem

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

rps_list = [rock, paper, scissors]

random_choice = random.randint(0, len(rps_list) - 1)
computer_choice = rps_list[random_choice]

if user_choice == 0: #rock
    print(rock)
    if computer_choice == rock:
        print(f"Computer chose: \n {computer_choice} \n It's a draw.")
    elif computer_choice == paper:
        print(f'Computer chose: \n {computer_choice} \n You lose')
    else:
        print(f'Computer chose: \n {computer_choice} \n You win!')

elif user_choice == 1: #paper
    print(paper)
    if computer_choice == rock:
        print(f'Computer chose: \n {computer_choice} \n You win!')
    elif computer_choice == paper:
        print(f"Computer chose: \n {computer_choice} \n It's a draw.")
    else:
        print(f'Computer chose: \n {computer_choice} \n You lose')

elif user_choice == 2: #scissors
    print(scissors)
    if computer_choice == rock:
        print(f'Computer chose: \n {computer_choice} \n You lose')
    elif computer_choice == paper:
        print(f'Computer chose: \n {computer_choice} \n You win!')
    else:
        print(f"Computer chose: \n {computer_choice} \n It's a draw.")

else:
    print('You typed and invalid number, You lose!')

#another solution to this problem

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    print('Computer Chose:')
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")