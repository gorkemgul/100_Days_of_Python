# ==================================================================================================================== #
#                                          The Day 7 Project: The Hangman                                              #
# ==================================================================================================================== #

# Import dependencies
import random
from hangmanStages import stages, logo
from hangmanWords import wordList

# Chose a random word from the word list
chosenWord = random.choice(wordList)

# Get the length of the chosen word
wordLength = len(chosenWord)

# Print the logo out
print(logo)

# Create the necessary blanks
display = []
for _ in range(wordLength):
    display += '_'

# Create a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen word which means display has no more blanks
end_of_game = False
lives = 6

while not end_of_game:
    # Get a letter from the user
    guess = input('Guess a letter:\n').lower()

    # Check if the user has already guessed it
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check the guessed letter
    for position in range(wordLength):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter

    # Check if the letter that user chose is wrong
    if guess not in chosenWord:
        print(f"You guessed {guess}, that's not in the word. Thus, you lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('GAME OVER!')

    # Join all the elements of the list & turn it into a string
    print(f"{' '.join(display)}")

    # Check if the user has got all the letters
    if '_' not in display:
        end_of_game = True
        print('Congrats!, You won the game!')

    # Print the stages out
    print(stages[lives])