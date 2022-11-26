# -*- encoding: utf-8 -*-
'''
@File    :   5-7-0.py
@Time    :   18/09/2022, 22:18:57
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def next_buses(current_time:int, timetable:list, how_many:int):
    """
    param : prints next n leaving bus times
    return: none
    """
    printed:int = 0
    round:int = 0

    print("The next buses leave:")

    while printed < how_many:
        # complex, but i am too dumb to do it otherwise
        for val in timetable:
            # next day case accept any time
            if round > 0: 
                if val >= 0 and printed < how_many:
                    print(val)
                    printed += 1
            else:
                if val >= current_time and printed < how_many:
                    print(val)
                    printed  += 1

        round += 1

def main():
    timetable:list = [630, 1015, 1415, 1620, 1720, 2000]
    time:int
    how_many:int = 3
    debug:bool = False

    if debug:
        time = 1720        
    else:
        time = int(input("Enter the time (as an integer): "))

    next_buses(time, timetable, how_many)

if __name__ == "__main__":
    main()
