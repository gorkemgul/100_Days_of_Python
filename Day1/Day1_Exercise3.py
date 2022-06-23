# ========================================================================= #
#               Day 1 Interactive Exercise 3 Input Function                 #
# ========================================================================= #

# We're going to write a program that prints the number of characters in user's name.

print(len(input("What is your name? ")))

#another way to do it

username = input("What is your name?\n")
length_of_username = len(username)
print(length_of_username)