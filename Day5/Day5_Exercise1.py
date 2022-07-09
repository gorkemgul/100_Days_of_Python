# ========================================================================= #
#                Day 5 Interactive Exercise 1 Average Height                #
# ========================================================================= #

# We're going to write a program that calculates the average student height from a List of heights.
# We're not allowed to use sum() or len() functions in our program.

student_heights = input('Input a list of student heights ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = 0
summation = 0
for height in student_heights:
    summation += height
    number_of_students += 1

result = round(summation / number_of_students)
print(result)