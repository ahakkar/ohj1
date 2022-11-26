# -*- encoding: utf-8 -*-
'''
@File    :   9-6.py
@Time    :   24/10/2022, 21:09:20
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def data_to_dict(data:list) -> dict:
    """
    param : TODO
    return: none
    """
    
    contacts:dict = {}
    col_names = data[0].strip().split(";")    
    data.pop(0)
           
    for row in data:        
        split_row = row.strip().split(";")
        contacts[split_row[0]] = {}
        # 0 key (nickname), 1 name, 2 phone, 3 email, 4 skype
        for i in range (1, len(col_names)):              
            contacts[split_row[0]][col_names[i]] = split_row[i]                  
        
    return contacts

def read_file(filename:str) -> dict:
    """
    param : TODO
    return: none
    """
    try:
        with open (filename, "r") as read_file:
            data:list = read_file.readlines()  
        read_file.close()
    except OSError:
        print("bad file name!")
        return
    
    return data_to_dict(data)

def main():
    info = read_file("contacts.csv")  

if __name__ == "__main__":
    main()
