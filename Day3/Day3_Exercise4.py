# ========================================================================= #
#                Day 3 Interactive Exercise 4 Pizza Order                   #
# ========================================================================= #

# We're going to write an automatic pizza order program.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
    bill = bill + 15
elif size == 'M':
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == 'Y':
    bill = bill + 1

print(f'Your final bill is: ${bill}.')
