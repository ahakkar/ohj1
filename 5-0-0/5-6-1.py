# -*- encoding: utf-8 -*-
'''
@File    :   5-6-1.py
@Time    :   18/09/2022, 22:11:23
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def convert_grades(numbers:list):
    """
    param : TODO
    return: none
    """

    amt:int = len(numbers)
    i:int = 0

    if amt == 0:
        return None
    else:
        while i < amt:
            if numbers[i] != 0:
                numbers[i] = 6
            i += 1


def main():
    debug:bool = False

    if debug:
        grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
        convert_grades(grades)
        print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

if __name__ == "__main__":
    main()
