# ========================================================================= #
#                      Day 2 Project: Tip Calculator                        #
# ========================================================================= #

#   We're going to write a program that calculates how much tips that every person will give
# - Firstly, We are going to write the name of our program
# - Secondly, We are gonna get necessary data from users
# - Finally, We are gonna do necessary numerical calculations

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
num_of_people = int(input('How many people to split the bill? '))

calculated_tip = tip / 100 * bill + bill
bill_per_person = calculated_tip / num_of_people
total_bill = round(bill_per_person, 2)
print(f'Each person should pay: ${total_bill}')