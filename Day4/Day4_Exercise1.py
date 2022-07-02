# ========================================================================= #
#               Day 4 Interactive Exercise 1 Heads or Tails                 #
# ========================================================================= #

# We're going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.


import random

number = random.randint(0,1)

if number == 1:
    print('Heads')
else:
    print('Tails')