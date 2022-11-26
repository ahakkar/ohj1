# -*- encoding: utf-8 -*-
'''
@File    :   6-7-0.py
@Time    :   18/09/2022, 23:17:11
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def create_an_acronym(string:str):
    """
    param : TODO
    return: none
    """
    acronym:str = ""
    words:list = string.split(" ")

    for word in words:
        acronym += word[0].upper()

    return acronym


def main():
    debug:bool = False
    if debug:
        print(create_an_acronym("central intelligence agency"))

if __name__ == "__main__":
    main()
