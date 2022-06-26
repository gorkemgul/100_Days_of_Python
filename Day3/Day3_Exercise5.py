# ========================================================================= #
#              Day 3 Interactive Exercise 4 Love Calculator                 #
# ========================================================================= #

# We're going to write a program that tests the compatibility between two people.
#  To work out the love score between two people;
# - Firstly, we're going to take both people's names and check for the number of times the letters in the word TRUE occurs.
# - Secondly, that we're gonna check for the number of times the letters in the word LOVE occurs.
# - Finally, We're going to combine these numbers to make a 2 digit number.

#taking data from user
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
lower_name = name.lower()

counted_chars1 = lower_name.count('t') + lower_name.count('r') + lower_name.count('u') + lower_name.count('e')
counted_chars2 = lower_name.count('l') + lower_name.count('o') + lower_name.count('v') + lower_name.count('e')

total = str(counted_chars1) + str(counted_chars2)
love_score = int(total)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')