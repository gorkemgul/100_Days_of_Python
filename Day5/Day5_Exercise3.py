# ========================================================================= #
#                 Day 5 Interactive Exercise 3 Adding Even                  #
# ========================================================================= #

# We're going to write a program that calculates the sum of all the even numbers from 1 to 100.

# My solution
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(f'Summation of all even numbers is: {total}')

# Alternative solution to this problem
total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(f'Summation of all even numbers is: {total2}')