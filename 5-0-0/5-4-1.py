# -*- encoding: utf-8 -*-
'''
@File    :   5-4-1.py
@Time    :   18/09/2022, 18:39:30
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def search_from_list(search:int, numbers:list):
    """
    param : number to be searched, list of numbers collected from user
    return: none
    """
    found:int = 0

    for i in numbers:   
        if search == i:
            found += 1

    if found > 0:
        print(f"{search} shows up {found} times among the numbers you have entered.")
    else:
        print(f"{search} is not among the numbers you have entered.")


def input_to_list(amount:int):
    """
    param : amount of numbers to be collected from user
    return: list
    """

    i:int = 0
    numbers:list = []
    print(f"Enter {amount} numbers:")

    while i < amount:
        numbers.append(int(input("")))
        i += 1
    
    return numbers


def main():
    amount:int
    search:int
    numbers:list = []

    amount = int(input("How many numbers do you want to process: "))
    numbers = input_to_list(amount)

    search = int(input("Enter the number to be searched: "))
    search_from_list(search, numbers)

if __name__ == "__main__":
    main()
