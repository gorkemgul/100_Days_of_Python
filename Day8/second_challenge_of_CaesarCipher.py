# ============================================================================================================== #
#                     The Second Challenge of The Day 8 Project: Reorganising Our Program                        #
# ============================================================================================================== #

# Create the alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get the inputs from the user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine those two functions called encrypt & decrypt into  a single function called Caesar
def Caesar(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for letter in startText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        endText += alphabet[newPosition]
    print(f"The {cipherDirection}d text is {endText}")

# Use the Caesar function that we created above
Caesar(startText = text, shiftAmount = shift, cipherDirection = direction)