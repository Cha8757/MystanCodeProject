"""
File: BeeperRowAdv.py
Name: TODO:
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *


def main() :
    """
    Karel will fill the first Street in any world
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
