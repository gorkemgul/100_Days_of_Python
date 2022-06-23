# ========================================================================= #
#                    Day 1 Project: Band Name Generator                     #
# ========================================================================= #

# We're gonna write a program that creates a band name for new bands
#   We're gonna follow these steps;
# - Firstly, We are going to write the name of our program
# - Secondly, We are going to take the name of the city that users grew up in & take the name of the pet of them
# - Finally, We are gonna combine our inputs to create a band name

print('Welcome to the Band Name Generator.')
city_name = input("What's the name of the city you grew up in?\n")
pets_name = input("What's your pet's name?\n")
combined_name = city_name + ' ' + pets_name
print("Your band name could be" + ' ' + combined_name)

