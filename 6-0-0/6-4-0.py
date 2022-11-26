# -*- encoding: utf-8 -*-
'''
@File    :   6-4-0.py
@Time    :   18/09/2022, 22:40:25
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def count_wovels(word:str):
    """
    param : count wovels and consonants of a word
    return: none
    """

    wovels:list = ['a','e','i','o','u','y']
    chr_amt:int = len(word)
    w_count = 0

    for char in word:
        if char in(wovels):
            w_count += 1

    print(f"The word \"{word}\" contains {w_count} vowels and {chr_amt-w_count} consonants.")



def main():
    debug:bool = False
    user_input:str    

    if debug:
        count_wovels("sassafrass")
    else:
        user_input = input("Enter a word: ")
        count_wovels(user_input)

if __name__ == "__main__":
    main()
