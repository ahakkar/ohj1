# -*- encoding: utf-8 -*-
'''
@File    :   7-7.py
@Time    :   21/10/2022, 20:31:42
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   More features to turistisanakirja
'''

def print_contents(dicionary:dict, in_same_row:bool = False, both_languages:bool = False) -> None:
    """
    param : dict
    return: none
    """
    
    abc:list = sorted(dicionary)
    if in_same_row:
        row: str = ""
        for key in abc:  
            row += key + ", "
        print(row.rstrip(", "))
    elif both_languages:
        print("\nEnglish-Spanish")
        for key in abc:  
            print(key, dicionary[key])
        
        print("\nSpanish-English")
        new_dict = {}
        for x, y in dicionary.items():
            new_dict[y] = x
            
        abc:list = sorted(new_dict)
        for key in abc:  
            print(key, new_dict[key]) 
        print()           
    
    else:        
        for key in abc:  
            print(key, dicionary[key])
            
def remove_word(dictionary:dict) -> dict:
    user_input = input("Give the word to be removed: ")
    if user_input in dictionary:
        del dictionary[user_input]
    else:
        print(f"The word {user_input} could not be found from the dictionary.")
        
    return dictionary

def translate_text(dictionary) -> None:
    """
    param : TODO
    return: none
    """                   
    
    user_input = input("Enter the text to be translated into Spanish: ")
    if len(user_input) > 0:                
        wordlist:list = user_input.split(" ")   
        translated:str = ""         
        for word in wordlist:
            if word in dictionary:
                translated += dictionary[word] + " "
            else:
                translated += word + " "
                
        print("The text, translated by the dictionary:")
        print(translated.rstrip())   
        
def translate_word(dictionary) -> None:
    """
    param : TODO
    return: none
    """
    
    user_input = input("Enter the word to be translated: ")
    if user_input in dictionary:             
        print(f"{user_input} in Spanish is {dictionary[user_input]}")
    else:
        print(f"The word {user_input} could not be found from the dictionary.")
        
def add_translation(dictionary) -> dict:
    """
    param : TODO
    return: none
    """
    
    input_lang1 = input("Give the word to be added in English: ")            
    input_lang2 = input("Give the word to be added in Spanish: ")
    
    if len(input_lang1) > 0 and len(input_lang2) > 0:
        dictionary[input_lang1] = input_lang2
        print("Dictionary contents:")
        print_contents(dictionary, True, False)
    

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}  
    print("Dictionary contents:")
    print_contents(english_spanish, True, False) 

    while True:        
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        match command.lower():
            case "w":   # translate word
                translate_word(english_spanish)
            
            case "a":   # add translation
                english_spanish = add_translation(english_spanish)
            
            case "r":   # remove word
                english_spanish = remove_word(english_spanish)            
              
            case "p":   # print dict  
                print_contents(english_spanish, False, True)                
            
            case "t":   # translate sentence
                translate_text(english_spanish)         

            case "q":   # quit program
                print("Adios!")
                return
            
            case _:
                print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
