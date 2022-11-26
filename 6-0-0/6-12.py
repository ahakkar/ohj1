# -*- encoding: utf-8 -*-
'''
@File    :   6-12.py
@Time    :   19/09/2022, 00:00:45
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def count_abbas(txt:str):
    """
    param : TODO
    return: none
    """
    txt_len = len(txt)
    index:int = 0 
    i:int = 0   
    count:int = 0

    if len(txt) < 4:
        return 0

    while i <= (txt_len - 4):
        if txt[i:i+4] == "abba":
            count += 1

        i +=1

    return count

