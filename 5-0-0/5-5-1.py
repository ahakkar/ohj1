# -*- encoding: utf-8 -*-
'''
@File    :   5-5-1.py
@Time    :   18/09/2022, 18:51:05
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def are_all_members_same(members:list):
    """
    param : list to check for sameness
    return: bool, are all indexes same or not
    """

    same:bool = True

    for mem in members:
        if members[0] != mem:
            same = False
            break

    return same

def main():
    debug = True

    if debug:
        members = [2, 2, 2]
        print(are_all_members_same(members))

        members = [2, 2, 3]
        print(are_all_members_same(members))

        members = ["Aku", "Aku", "Aku"]
        print(are_all_members_same(members))

        members = ["Tupu", "Hupu", "Lupu"]
        print(are_all_members_same(members))

if __name__ == "__main__":
    main()
