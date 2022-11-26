# -*- encoding: utf-8 -*-
'''
@File    :   5-2-0.py
@Time    :   18/09/2022, 18:22:49
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def loop():
    """
    param :
    return: none
    """
    i = 0

    for i in range(0, 102, 2):
        print(i)

    i = 100

    for i in range(100, -2, -2):
        print(i)

def main():
    loop()

if __name__ == "__main__":
    main()
