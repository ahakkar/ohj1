# -*- encoding: utf-8 -*-
'''
@File    :   5-3-2.py
@Time    :   18/09/2022, 18:35:40
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def print_last_from_first(numbers):
    """
    param : list of numbers collected from user
    return: none
    """
    print("The numbers you entered, in reverse order:")

    for i in range(len(numbers)-1,-1,-1):        
        print(numbers[i])


def user_input(amount:int):
    """
    param : amount of numbers to be collected from user
    return: none
    """

    i:int = 0
    numbers:list = []

    print(f"Give {amount} numbers: ")
    while i < amount:
        numbers.append(int(input("Next number: ")))
        i += 1
    
    print_last_from_first(numbers)


def main():
    amount:int = 5
    user_input(amount)

if __name__ == "__main__":
    main()
