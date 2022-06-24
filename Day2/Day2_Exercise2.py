# ========================================================================= #
#               Day 2 Interactive Exercise 2 BMI Calculator                 #
# ========================================================================= #

# We're going to write a program that calculates the Body Mass index (BMI) from a user's weight and height
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

#the first solution of this problem
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

bmi = int(weight) / float(height) ** 2
print(int(bmi))

#the second solution of this problem
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
