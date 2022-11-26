# -*- encoding: utf-8 -*-
'''
@File    :   8-13.py
@Time    :   24/10/2022, 17:10:54
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

def print_score(data:list):
    """
    data: list of all rows in user specified file
    return: none
    """
    score:dict = {}
    
    for row in data:        
        row = row.rstrip()       
        items:list = row.split(" ")
        
        if len(items) != 2:
            print("There was an erroneous line in the file:")
            print(row)
            return
        
        try:
            points = int(items[1])            
        except ValueError:
            print("There was an erroneous score in the file:")
            print(items[1])
            return
        
        if items[0] in score:
            score[items[0]] += points
        else:
            score[items[0]] = points

    # print score
    print("Contestant score:")
    abc:list = sorted(score)
    for key in abc:
        print(key, score[key])
                

def main():
    filename = input("Enter the name of the score file: ")

    try:
        with open(filename, mode="r") as read_file:
            data:list = read_file.readlines()                    
    except OSError:
        print(f"There was an error in reading the file.")
        return    
            
    print_score(data)
    
if __name__ == "__main__":
    main()