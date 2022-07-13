# =================================================================================================== #
#                Day 6 Project: Escaping The Maze              #
# =================================================================================================== #

# We're going to write a program that will help to reeborg to espace from the maze.
# It can be open from this link:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# It has a couple of defined functions. But we're also going to define a function to turn right.
# Indeed, The maze will be created randomly. So, we have to write our program by considering this situation.
# All the codes that I wrote here, can be only run on the website.

# define a function to turn right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()