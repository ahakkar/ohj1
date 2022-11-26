# -*- encoding: utf-8 -*-
'''
@File    :   6-6-0.py
@Time    :   18/09/2022, 22:47:46
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def reverse_name(name:str):
    """
    param : reverses ln,fn, strips whitespace
    return: fixed name
    """
    if "," not in name:
        return name

    fixed_name:str = ""

    items = name.split(",")
    items[0] = items[0].strip()
    items[1] = items[1].strip()

    if len(items[1]) > 0:
        fixed_name += items[1]
    if len(fixed_name) > 0 and len(items[0]) > 0:
        fixed_name += f" {items[0]}"
    elif len(items[0]) > 0:
        fixed_name += items[0]
 
    return fixed_name 

def main():
    debug:bool = False
    if debug:
        print(reverse_name("Techie, Teddy"))
        print(reverse_name("Scumble,    Arnold"))
        print(reverse_name("Fortunato,Frank"))
        print(reverse_name("von Grünbaumberger, Herbert"))
        print(reverse_name("   Duck,     Donald  "))
        print(reverse_name("X,"))
        print(reverse_name(",X"))
        print(reverse_name(" , Y "))

if __name__ == "__main__":
    main()
