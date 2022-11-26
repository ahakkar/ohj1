# -*- encoding: utf-8 -*-
'''
@File    :   8-4.py
@Time    :   23/10/2022, 21:25:02
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def print_box(width, height, mark):
    """
    Enter the width of a frame: 6
    Enter the height of a frame: 3
    Enter a print mark: *

    ******
    ******
    ******
    """

    i = 0
    while i < height:
        print(mark * width)
        i += 1

def read_int(q: str):
    """
    Enter the width of a frame: -1
    Enter the width of a frame: 0
    Enter the width of a frame: -4
    Enter the width of a frame: 4
    Enter the height of a frame: -1
    Enter the height of a frame: 0
    Enter the height of a frame: 2
    Enter a print mark: #

    ####
    ####
    """

    while True:
        try:
            user_input = int(input(q))
            if user_input > 0:
                return user_input
        except ValueError:
            continue

def main():
    width = read_int("Enter the width of a frame: ")
    height = read_int("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
