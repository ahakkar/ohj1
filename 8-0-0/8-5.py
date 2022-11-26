# -*- encoding: utf-8 -*-
'''
@File    :   8-5.py
@Time    :   24/10/2022, 14:31:30
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''



def main():
    filename = input("Enter the name of the file: ")


    try:
        file = open(filename, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    i:int = 1
    for file_line in file:
        file_line = file_line.strip()
        print(f"{i} {file_line}")
        i += 1

    file.close()


if __name__ == "__main__":
    main()
