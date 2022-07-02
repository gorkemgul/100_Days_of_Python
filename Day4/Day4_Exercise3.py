# ========================================================================= #
#                Day 4 Interactive Exercise 3 Treasure Map                  #
# ========================================================================= #

# We're going to write a program that will mark a spot with an X
# We're going to create a map that contains a nested list.
# When map is printed this is what the nested list looks like this;
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# We're going to use new lines (\n) to format the three rows into a square, like this;
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

map[row][column] = 'X'
print(f"{row1}\n{row2}\n{row3}")
