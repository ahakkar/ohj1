# -*- encoding: utf-8 -*-
'''
@File    :   6-7-0.py
@Time    :   18/09/2022, 23:21:11
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def capitalize_initial_letters(string:str):
    """
    param : TODO
    return: none
    """
    capitalized:str = ""

    if len(string) == 0:
        return capitalized

    string = string.lower()
    words:list = string.split(" ")

    for word in words:        
        capitalized += word[0].upper() + word[1:] + " "

    return capitalized.rstrip(" ")


def main():
    debug:bool = False
    if debug:
        print(capitalize_initial_letters("drIVING cAR"))

if __name__ == "__main__":
    main()
