# ================================================================================================= #
#                Day 5 Interactive Exercise 4 The FizzBuzz Job Interview Question                   #
# ================================================================================================= #

# We're going to write a program that automatically prints the solution to the FizzBuzz game.
# Our program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print 'Fizz'.
# When the number is divisible by 5 then instead of printing the number it should print 'Buzz'.
# Last but not least, if the number is divisible by both 3 and 5 e.g 15 then instead of printing the number it should print 'FizzBuzz'.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)