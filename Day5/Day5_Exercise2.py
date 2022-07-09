# ========================================================================= #
#                  Day 5 Interactive Exercise 2 High Score                  #
# ========================================================================= #

# We're going to write a program that calculates the highest score from a List of scores.
# We're not allowed to use max() function in our program.

student_scores = input('Input a list of student scores ').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f'The highest score in the class is: {highest_score}')