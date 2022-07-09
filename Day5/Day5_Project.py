# ========================================================================= #
#                    Day 5 Project: Password Generator                      #
# ========================================================================= #

# We're going to write a program that creates a password for users.
# Firstly, We're going to take a couple of inputs from users.
# Secondly, According to those inputs, the program is going to choose symbols, characters & numbers from their lists randomly.
# Finally, Based on those choices, It's going to create a password.
# Note: There will be two versions of generators. One of them is for easy passwords and the other one will be for hard password creation.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#My solution to this problem

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letter = ''
random_symbol = ''
random_number = ''
for letter in range(1, nr_letters + 1):
    random_letter += letters[random.randint(0, len(letters) - 1)]
for symbol in range(1, nr_symbols + 1):
    random_symbol += symbols[random.randint(0, len(symbols) - 1)]
for number in range(1, nr_numbers + 1):
    random_number += numbers[random.randint(0, len(numbers) - 1)]

easy_pass = random_letter + random_symbol + random_number


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
shuffled_list = random.sample(easy_pass, len(easy_pass))
hard_pass = ''
for c in shuffled_list:
    hard_pass += c

#Another solution to this problem

#For Easy Level
easy_pass2 = ''
for char in range(1, nr_letters + 1):
    easy_pass2 += random.choice(letters)
for char in range(1, nr_symbols + 1):
    easy_pass2 += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    easy_pass2 += random.choice(numbers)

#For Hard Level
hard_pass2 = []
for char in range(1, nr_letters + 1):
    hard_pass2.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    hard_pass2.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    hard_pass2.append(random.choice(numbers))
random.shuffle(hard_pass2)
password2 = ''
for char in hard_pass2:
    password2 += char
print(f'Your password is: {password2}')