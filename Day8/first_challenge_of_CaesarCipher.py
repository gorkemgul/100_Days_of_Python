# ============================================================================================================== #
#                      The First Challenge of The Day 8 Project: Encryption & Decryption                         #
# ============================================================================================================== #

# Define an alphabet list composed of the letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get the inputs from the user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Define a function called encrypt that takes the text & shift as inputs
def encrypt(plainText, shiftAmount):
    cipherText = ""
    for letter in plainText:
        oldIdx = alphabet.index(letter)
        newIdx = oldIdx + shiftAmount
        cipherText += alphabet[newIdx]
    print(f"The encoded text is {cipherText}")

# Define a function called decrypt that takes the text & shift as inputs
def decrypt(cipherText, shiftAmount):
    plainText = ""
    for letter in cipherText:
        oldIdx = alphabet.index(letter)
        newIdx = oldIdx - shiftAmount
        plainText += alphabet[newIdx]
    print(f"The decoded text is {plainText}")

# Check if user wants to encode or decode
if direction == 'encode':
    encrypt(plainText = text, shiftAmount = shift)
elif direction == 'decode':
    decrypt(cipherText = text, shiftAmount = shift)