# ========================================================================= #
#                      Day 3 Project: Treasure Island                       #
# ========================================================================= #

# We're going to write a program named Treasure Island. It's content going to be like choose your adventure books.
# Users are going to make choices, depending on their decisions they will get results.
# The game will continue till they make wrong decisions
# - if they choose right at first, they will lose the game.
# - after they passed the first place, if they choose swim they will lose the game.
# - and again if they pass the second place and if they choose Red & Blue they will lose the game.


print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

first_question = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if first_question == 'left':
    second_question = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if second_question == 'wait':
        final_question = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
        if final_question == 'yellow':
            print('Congrats! You found the treasure! You Win!')
        elif final_question == 'red':
            print("It's a room full of fire. Game Over.")
        elif final_question == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print('You fell into a hole. Game Over.')

