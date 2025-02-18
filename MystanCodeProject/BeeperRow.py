"""
File: BeeperRow.py
Name: TODO:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    turn_left()
    move()
    pick_beeper()
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    put_beeper()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
