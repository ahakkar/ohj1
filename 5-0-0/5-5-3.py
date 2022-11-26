# -*- encoding: utf-8 -*-
'''
@File    :   5-5-3.py
@Time    :   18/09/2022, 22:01:15
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def calc_score(results:list):
    """
    param : list of rubik results in secs
    return: none
    """
    score:float

    results.sort()      #sort ASC
    del results[0]      #remove smallest time
    del results[-1]     #remove largest time

    score = sum(results) / len(results) #calc avg time

    print(f"The official competition score is {score:.2f} seconds.")


def input_to_list(amount:int):
    """
    param : amount of numbers to be collected from user
    return: list
    """

    i:int = 0
    numbers:list = []

    while i < amount:
        numbers.append(float(input(f"Enter the time for performance {i+1}: ")))
        i += 1
    
    return numbers

def main():
    debug:bool = False

    perf:list = []

    if debug:
        perf = [5.80, 5.40, 5.17, 5.19, 5.22]        
    else:
        perf = input_to_list(5)

    calc_score(perf)

if __name__ == "__main__":
    main()
