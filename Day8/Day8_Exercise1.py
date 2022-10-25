# =============================================================================== #
#              Day 8 Interactive Exercise 1: Paint Area Calculator                #
# =============================================================================== #

# Import the math library
import math

# Define the function to calculate the number of cans
def paint_cal(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

# Get the information from the user
testHeight = int(input('Height of the wall:\n'))
testWidth = int(input('Width of the wall:\n'))

# 1 can of paint can cover 5 square
coverage = 5

# Use the function to calculate number of cans
paint_cal(height = testHeight, width = testWidth, cover = coverage)







