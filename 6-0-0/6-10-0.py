# -*- encoding: utf-8 -*-
'''
@File    :   6-10-0.py
@Time    :   18/09/2022, 23:48:27
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def read_message():
    """
    param : TODO
    return: none
    """

    msg:list = []
    user_input:str

    while True:
        user_input = input()
        if user_input == "":
            break
        
        msg.append(user_input)

    return msg 

def print_uppercase(msg:list):
    """
    param : TODO
    return: none
    """   
    for row in msg:
        print(row.upper())

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    print_uppercase(msg)


if __name__ == "__main__":
    main()
