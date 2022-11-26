# -*- encoding: utf-8 -*-
'''
@File    :   5-5-2.py
@Time    :   18/09/2022, 18:55:53
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def is_the_list_in_order(check:list):
    """
    param : TODO
    return: bool
    """

    asc:bool = True
    entries:int = len(check)
    i:int = 0

    while i < entries-1: #dont want to compare last index to an out of range idnex
        if check[i] > check[i+1]:
            asc = False
            break
        i +=1

    return asc

def main():
    debug:bool = False
    if debug:
        print(is_the_list_in_order([37, 42, 43]))
        print(is_the_list_in_order([42, 37, 43]))

if __name__ == "__main__":
    main()
