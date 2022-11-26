# -*- encoding: utf-8 -*-
'''
@File    :   6-9-0.py
@Time    :   18/09/2022, 23:28:27
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


def main():
    debug:bool = False
    result:str
    if debug:
        result = row_encryption("Happy, happy, joy, joy!")
        print(result)
        print(row_encryption(result))
        encrypt(' ')
        encrypt('?')

if __name__ == "__main__":
    main()
