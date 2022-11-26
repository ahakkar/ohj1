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

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}  
    print("Dictionary contents:")
    print_contents(english_spanish, True, False) 

    while True:        
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command.lower() == "w":

            user_input = input("Enter the word to be translated: ")
            if user_input in english_spanish:             
                print(f"{user_input} in Spanish is {english_spanish[user_input]}")
            else:
                print(f"The word {user_input} could not be found from the dictionary.")

        elif command.lower() == "a":
            input_en = input("Give the word to be added in English: ")            
            input_es = input("Give the word to be added in Spanish: ")
            
            if len(input_en) > 0 and len(input_es) > 0:
                english_spanish[input_en] = input_es
                print("Dictionary contents:")
                print_contents(english_spanish, True, False)

        elif command.lower() == "r":
            user_input = input("Give the word to be removed: ")
            if user_input in english_spanish:
                del english_spanish[user_input]
            else:
                print(f"The word {user_input} could not be found from the dictionary.")
                
        elif command.lower() == "p":
            print_contents(english_spanish, False, True)
                
        elif command.lower() == "t":
            user_input = input("Enter the text to be translated into Spanish: ")
            if len(user_input) > 0:                
                wordlist:list = user_input.split(" ")   
                translated:str = ""         
                for word in wordlist:
                    if word in english_spanish:
                        translated += english_spanish[word] + " "
                    else:
                        translated += word + " "
                        
                print("The text, translated by the dictionary:")
                print(translated.rstrip())
            

        elif command.lower() == "q":
            print("Adios!")
            return
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
