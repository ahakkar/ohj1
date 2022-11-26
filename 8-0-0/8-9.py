# -*- encoding: utf-8 -*-
'''
@File    :   8-9.py
@Time    :   24/10/2022, 14:46:54
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def ask_rows():
    rows:list = []
    
    print("Enter rows of text. Quit by entering an empty row.")
    
    # read rows from user to 1 list
    while True:
        try:
            row:str = input()            
        except ValueError:
            print("Bad input!")
            continue 
        
        if row == "":
            break
        
        row = row.strip()
        rows.append(row)       
        
    # save all gathered rows to str    
    data:str = ""
    i:int = 1
    for row in rows:
        data += f"{i} {row}\n"
        i += 1

    return data

def main():
    filename = input("Enter the name of the file: ")

    try:
        with open(filename, mode="w") as save_file:
            data:list = ask_rows()
            save_file.write(data)  
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return    
            
    print(f"File {filename} has been written.")
    
if __name__ == "__main__":
    main()