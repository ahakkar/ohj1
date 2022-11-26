"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
3-8-1
"""

import math

def area(a: int, b:int, c:int):
    """
    using heron's formula
    https://en.wikipedia.org/wiki/Heron's_formula
    side lengths in list
    0 = a
    1 = b
    2 = c
    """
    semi = (a+b+c)/2
    area = math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))

    return area

def main():
  
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))


    print(f"The triangle's area is {area(a, b, c):.1f}")


if __name__ == "__main__":
    main()

