"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
3-6-3
"""

def print_box(width, height, mark):
    """
    Enter the width of a frame: 6
    Enter the height of a frame: 3
    Enter a print mark: *

    ******
    ******
    ******
    """

    i = 0
    while i < height:
        print(mark * width)
        i += 1

def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
