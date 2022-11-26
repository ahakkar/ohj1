# -*- encoding: utf-8 -*-
'''
@File    :   6-11.py
@Time    :   18/09/2022, 23:55:52
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

REGULAR_CHARS   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                    "w", "x", "y", "z"]

ENCRYPTED_CHARS = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                    "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                    "j", "k", "l", "m"]

def encrypt(char:str):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
   
    # don't try to encrypt invalid chars
    if not char.lower() in REGULAR_CHARS:
        return char

    # check case
    upper_case:bool = True
    if not char.isupper():
        upper_case = False

    # for search put char to lower case
    char = char.lower()
    index:int = REGULAR_CHARS.index(char)    

    enc_char:str = ENCRYPTED_CHARS[index]

    # restore original case
    if upper_case:
        enc_char = enc_char.upper()

    return enc_char

def row_encryption(text:str):
    """
    Encrypts string with ROT13
    param : string, as text
    return: string, encrypted 
    """
    enc_text:str = ""

    for char in text:
        if char.lower() in REGULAR_CHARS:
            enc_text += encrypt(char)
        else:
            enc_text += char

    return enc_text

def encrypt_rows(msg:list):
    """
    param : TODO
    return: none
    """   
    for row in msg:
        print(row_encryption(row))

def read_message():
    """
    reads row from users and adds them to a list, stops at empty row
    param : none
    return: list, read rows
    """

    msg:list = []
    user_input:str

    while True:
        user_input = input()
        if user_input == "":
            break
        
        msg.append(user_input)

    return msg 


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    #msg:list = ["Puff, the magic dragon lived by the sea,", "And frolicked in the autumn mist, in a land called Honah Lee."]

    print("ROT13:")
    encrypt_rows(msg)


if __name__ == "__main__":
    main()
