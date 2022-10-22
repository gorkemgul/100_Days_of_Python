# ==================================================================================================================== #
#                  The Fourth Challenge of The Day 7 Project: Keeping Track of The Player's Lives                      #
# ==================================================================================================================== #

# Import dependencies
import random

# Create the stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Create a word list to pick a random word each time
wordList = ['melon', 'camel', 'apple']

# Chose a random word from the word list
chosenWord = random.choice(wordList)

# Create an empty list & add '_' as much as letters that chosen word has
display = []
for _ in range(len(chosenWord)):
    display += '_'

# Create a variable called 'lives' to keep track of the number of lives left & Set it to equal 6
lives = 6

# Create a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen word which means display has no more blanks
end_of_game = False

while not end_of_game:
    # Ask user to get a letter
    guess = input('Guess a letter!\n').lower()

    # Check the guessed letter
    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter

    # Check if the letter that user chose is wrong
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('GAME OVER!')

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if the user has got all the letters
    if '_' not in display:
        end_of_game = True
        print('You won the game!')

    # Print the stages out
    print(stages[lives])