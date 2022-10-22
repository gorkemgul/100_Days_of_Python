# ======================================================================================================================= #
#                  The First Challenge of The Day 7 Project: Picking Random Words & Checking Answers                      #
# ======================================================================================================================= #

# Import dependencies
import random

# Create a word list to pick a random word each time
wordList = ['melon', 'camel', 'apple']

# Chose a random word from the word list
chosenWord = random.choice(wordList)

# Ask user to guess a letter
guess = input('Guess a letter!\n').lower()

# Check if the letter that user guesses is one of the letters in the chosen word
for letter in chosenWord:
    if letter == guess:
        print("Yes, it matches.")
    else:
        print('No, it does not match!')