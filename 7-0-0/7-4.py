# -*- encoding: utf-8 -*-
'''
@File    :   7-4.py
@Time    :   21/10/2022, 19:46:04
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Turistisanakirja matkalle
'''

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

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

        elif command.lower() == "r":
            user_input = input("Give the word to be removed: ")
            if user_input in english_spanish:
                del english_spanish[user_input]
            else:
                print(f"The word {user_input} could not be found from the dictionary.")
                
        elif command.lower() == "p":
            abc:list = sorted(english_spanish)
            for key in abc:
                print(key, english_spanish[key])
                
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
