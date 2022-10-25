# =============================================================================== #
#               Day 8 Interactive Exercise 2: Prime Number Checker                #
# =============================================================================== #

# Create a function that detects if given number is prime or not
def primeChecker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Get the number from the user
number = int(input("Check this number: "))

# Check if the number that user entered is a prime number
primeChecker(number = number)