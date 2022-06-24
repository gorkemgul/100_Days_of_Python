# ========================================================================= #
#                Day 2 Interactive Exercise 2 Life in Weeks                 #
# ========================================================================= #

# We are going to write a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input('What is your current age: ')

calculated_years_left = (90 - int(age))

days_left = calculated_years_left * 365
weeks_left = calculated_years_left * 52
months_left = calculated_years_left * 12

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')