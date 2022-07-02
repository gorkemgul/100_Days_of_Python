# =========================================================================================== #
#           Day 4 Interactive Exercise 2 Banker Roulette - Who will pay the bill?             #
# =========================================================================================== #

# We're going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# We're not allowed to use choice() function.

import random

#getting data from user and turning into list
names_string = input("Give me everboyd's names, separated by a comma. ")
names = names_string.split(', ')

random_number = random.randint(0, len(names) - 1)
random_name = names[random_number]

print(f'{random_name} is going to buy the meal today!')

#if we use choice() function

person_who_will_pay = random.choice(names)
print(person_who_will_pay + ' is going to buy the meal today!')

