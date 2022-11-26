"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
4-10-1
"""

def print_box(width:int, height:int, border_mark:str = "#", inner_mark:str = " "):
    """
    print box from submitted values
    return None
    """

    i = 0
    while i < height:
        if (i == 0) or (i == height-1):
            print(border_mark * width)
        else:
            print(f"{border_mark}{inner_mark*(width-2)}{border_mark}")

        i += 1

    return None

def read_input(q: str):
    """
    read user input 
    return valid input
    """

    while True:
        user_input = int(input(q))
        if user_input > 0:
            return user_input

def main():
    """
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    """

    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
