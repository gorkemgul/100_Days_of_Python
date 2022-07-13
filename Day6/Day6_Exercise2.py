# ================================================================================================= #
#                Day 6 Interactive Exercise 2 The Hurdles Challenge using While Loops               #
# ================================================================================================= #

# We're going to write a program that will make reeborg achieve his target.
# It can be open from this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# It has a couple of defined functions. But we're also going to define a couple of functions to solve this problem.
# But this time the goal will be placed randomly which means we have to check if we're at the goal. In order to check that there is a function named at_goal(). It's already defined on the website.
# Plus, The walls will be placed randomly as well. So we're gonna check if there is a wall before we make the robot move.
# All the codes that I wrote here, can be only run on the website.

#define a function to turn right
def turn_right():
    turn_left() #already defined on the website.
    turn_left()
    turn_left()

#define a function to jump over the walls.
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Check if we're at the goal. (at.goal(), wall_in_front() and front_is_clear() functions are also defined on the website.)
while not at.goal():
    if wall_in_front():
        jump()
    else:
        move()