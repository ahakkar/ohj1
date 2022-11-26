# -*- encoding: utf-8 -*-
'''
@File    :   7-13.py
@Time    :   23/10/2022, 21:06:28
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    abc:list = sorted(PRICES)

    new_dict = {}
    for x, y in PRICES.items():
        new_dict[y] = x
        
    abc:list = sorted(new_dict)
    for key in abc:  
        print(new_dict[key], f"{key:.2f}") 
    print()           


if __name__ == "__main__":
    main()
