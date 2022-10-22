# ============================================================================================================== #
#                  The Second Challenge of The Day 7 Project: Replacing Blanks with Guesses                      #
# ============================================================================================================== #

# Import dependencies
import random

# Create a word list to pick a random word each time
wordList = ['melon', 'camel', 'apple']

# Chose a random word from the word list
chosenWord = random.choice(wordList)

# Ask user to guess a letter
guess = input('Guess a letter!\n').lower()

# Create an empty list & add '_' as much as letters that chosen word has
display = []
for _ in range(len(chosenWord)):
    display += '_'

# Loop through each position in the chosen word & if the letter at that position matches 'guess' then reveal that letter in the display at that position
idx = 0
for letter in chosenWord:
    if letter == guess:
        display[idx] = letter
    idx += 1

# An alternative approach of looping through
# for position in range(len(chosenWord)):
#     letter = chosenWord[position]
#     if letter == guess:
#         display[position] = letter