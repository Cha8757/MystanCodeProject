"""
File: MoveToTheEnd.py
Name: TODO:
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end of the first Street in any world
    """
    for i in range(7):
        move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
