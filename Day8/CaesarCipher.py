# ============================================================================================================= #
#                                         Day 8 Project: Caesar Cipher                                          #
# ============================================================================================================= #

# Import dependencies
from CaesarCipherArt import logo

# Define the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the caesar function
def Caesar(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == 'decode':
        shiftAmount *= -1
    for char in startText:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shiftAmount
            endText += alphabet[newPosition]
        else:
            endText += char
    print(f"Here's the {cipherDirection}d result: {endText}")

# Print the logo out
print(logo)

# Use a while loop to check if the user wants to restart the cipher program
shouldContinue = True
while shouldContinue:
    # Get the inputs from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # In case, the user enters a shift that is greater than the number of letters in the alphabet
    shift = shift % 26

    # Use the Caesar function that we created above
    Caesar(startText = text, shiftAmount = shift, cipherDirection = direction)

    # Check if the user wants to continue or not
    result = input("Type 'yes' if you want to go again. Otherwise please type 'no'.\n")
    if result == 'no':
        shouldContinue = False
        print('Goodbye')