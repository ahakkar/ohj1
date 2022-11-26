# -*- encoding: utf-8 -*-
'''
@File    :   7-3-0.py
@Time    :   21/10/2022, 19:27:17
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Template for pricelist assignment.
'''

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        user_input = input("Enter product name: ")
        user_input = user_input.strip()
        
        if user_input in PRICES:
            print(f"The price of {user_input} is {PRICES[user_input]:.2f} e")        
        elif len(user_input) < 1:
            print("Bye!")
            return
        else:
            print(f"Error: {user_input} is unknown.")        


if __name__ == "__main__":
    main()
