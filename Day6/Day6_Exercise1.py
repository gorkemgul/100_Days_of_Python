# ===================================================================================== #
#                Day 6 Interactive Exercise 1 The Hurdles Loop Challenge                #
# ===================================================================================== #

# We're going to write a program that will make reeborg achieve his target.
# It can be open from this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# It has a couple of defined functions. But we're also going to define a couple of functions to solve this problem.
# All the codes that I wrote here, can be only used on the website.

#First solution to this problem.

#define a function to turn right.
def turn_right():
    turn_left() #turn_left function is already defined on the website.
    turn_left()
    turn_left()

#define a function to jump.
def jump():
    turn_left()
    move() #move is also already defined on the website.
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()
move()
jump()

#Better alternative to solve this problem.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump2():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()