# -*- encoding: utf-8 -*-
'''
@File    :   5-3-1.py
@Time    :   18/09/2022, 18:26:39
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def greater_than_zero(numbers):
    """
    param : list of numbers collected from user
    return: none
    """
    print("The numbers you entered that were greater than zero were:")

    for num in numbers:
        if num > 0:
            print(num)


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
    
    greater_than_zero(numbers)


def main():
    amount:int = 5
    user_input(amount)

if __name__ == "__main__":
    main()
