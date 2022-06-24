# ========================================================================= #
#                 Day 2 Interactive Exercise 1 Data Types                   #
# ========================================================================= #

# We're going to write a program that add the digits in a 2 digit number
# e.g if the input was 35 than the output should be 3 + 5 = 8

two_digit_number = input('Type a two digit number: ')

#the first solution to this problem
print(int(two_digit_number[0]) + int(two_digit_number[1]))

#the second solution to this problem
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)