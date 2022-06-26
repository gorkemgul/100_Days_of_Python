# ========================================================================= #
#                  Day 3 Interactive Exercise 2 BMI 2.0                     #
# ========================================================================= #

# We're going to write a program that interprets the Body Mass Index based on user's weight and height
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

height = float(input('enter your height in m: '))
weight = float(input('enter your weight in kg: '))

bmi = weight / height ** 2
rounded_bmi = round(bmi)

if rounded_bmi < 18.5:
    print(f'Your BMI is {rounded_bmi}, you are underweight.')
elif rounded_bmi < 25:
    print(f'Your BMI is {rounded_bmi}, you have a normal weight.')
elif rounded_bmi < 30:
    print(f'Your BMI is {rounded_bmi}, you are slightly overweight.')
elif rounded_bmi < 35:
    print(f'Your BMI is {rounded_bmi}, you are obese.')
else:
    print(f'Your BMI is {rounded_bmi}, you are clinically obese.')