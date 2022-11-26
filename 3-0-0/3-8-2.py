"""
COMP.CS.100 Programming 1
Print a box with input error checking
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

def read_input(q: str):
    """
    Enter the width of a frame: -1
    Enter the width of a frame: 0
    Enter the width of a frame: -4
    Enter the width of a frame: 4
    Enter the height of a frame: -1
    Enter the height of a frame: 0
    Enter the height of a frame: 2
    Enter a print mark: #

    ####
    ####
    """

    while True:
        user_input = int(input(q))
        if user_input > 0:
            return user_input

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
