"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
4-6-1
"""
import math

def ask_q(q):
    """
    asks above zero input from user
    returns input
    """
    user_input = float

    while True:
        user_input = float(input(q))
        if 0 >= user_input:
            continue
        else:
            break

    return user_input

def print_results(res):
    """
    prints results from list. assumes list has 2 entries.
    no returns
    """
    print(f"The circumference is {res[0]:.2f}")
    print(f"The surface area is {res[1]:.2f}")

def calc_area_s():
    """
    calculates square circ&area
    no params
    no returns
    """
    res = []
    len = ask_q("Enter the length of the square's side: ")
    
    res.append(len*4)    # circumference    
    res.append(len*len)  # area
    print_results(res)

def calc_area_r():
    """
    calculates rect circ&area
    no params
    no returns
    """
    res = [0, 0]
    lens = []
    i = 1

    while i < 3:
        lens.append(ask_q(f"Enter the length of the rectangle's side {i}: "))
        i += 1

    res[0] = lens[0]*2 + lens[1]*2
    res[1] = lens[0] * lens[1]

    print_results(res)

def calc_area_c():
    """
    calculates circle circ&area
    no params
    no returns
    """
    res = []
    len = ask_q("Enter the circle's radius: ")
    
    res.append(2 * math.pi * len)  # circumference    
    res.append(math.pi*(len*len))  # area
    print_results(res)

def completely_useless_function():
    """
    this function does not do anything
    """
    pass

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            calc_area_s()  
        elif answer == "r":
            calc_area_r()  
        elif answer == "c":
            calc_area_c()  
        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
