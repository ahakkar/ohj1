# -*- encoding: utf-8 -*-
"""
@File    :   6-13.py
@Time    :   19/09/2022, 00:12:57
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
"""

def longest_substring_in_order(text:str) -> str:
    """
    text  : string to search abc's from
    return: longest abc found from str
    """
    str_length:int = len(text)
    
    # validity checking    
    if str_length == 1 or text == "":
        return text
    
    i = 0
    substr = text[i]
    strings = []
    
    while i < str_length:
        #print(f"round {i}")

        # if last char in substring is the same as current char -1, it's next in abc's
        if text[i] > substr[-1]:
            #print("now saving", text[i])
            substr += text[i]
    
        # if char is not next in abc's
        else:
            strings.append(substr)
            substr = text[i]        
        i += 1
    
    # save last substring 
    if len(substr) > 1:
        strings.append(substr)  
           
    return search_for_first_in_abcs(strings)

def search_for_first_in_abcs(strings:list) -> str:
    """
    param : TODO
    return: none
    """
    
    longest_str: str = strings[0]    
         
    for string in strings:        
        if(len(string)) > len(longest_str):            
            longest_str = string    
           
    return longest_str

def main():
    debug:bool = False

    if debug:
        print(longest_substring_in_order("abcdfklmn"))      
        print(longest_substring_in_order("abcfdf"))
        print(longest_substring_in_order("abcabcdefgabab"))  
        print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
        print(longest_substring_in_order("ffgdfjkgabcdf"))          
        print(longest_substring_in_order("x"))
        print(longest_substring_in_order("aaa"))
        print(longest_substring_in_order('xyzstuopqklmefgabc'))
        print(longest_substring_in_order('acdkbarstyefgioprtyrtyx'))

if __name__ == "__main__":
    main()
