# -*- encoding: utf-8 -*-
'''
@File    :   6-14-0.py
@Time    :   16/10/2022, 00:29:39
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Justifies text rows to n chars
'''

SEPARATOR = " "

def get_text() -> tuple:
    """
    Reads rows of text from user,
    and reads row char limit
    
    param : none
    return: (list, int) words in a list, line length
    """
    user_rows: list = []
    wordlist: list = []
    chars_per_row = int  
         
    print("Enter text rows. Quit by entering an empty row.")
    
    # read input from user row by row, add rows to list
    while(True):
        user_input = input()
        if len(user_input) > 0:
            user_rows.append(user_input.split(SEPARATOR))
        else:
            chars_per_row = int(input("Enter the number of characters per line: "))           
            break
    
    # extract words from the row list and add them to a new wordlist
    for row in user_rows:
        for word in row:
            if len(word) > 0:      
                wordlist.append(word.strip())
                    
    return (wordlist, chars_per_row)

def justify(wordlist:list, max_chars_per_row: int) -> list:
    """
    Justifies a list of words. Adds words to a row until row is full,
    then justifies the row. Adds a justified row to a list.
    
    wordlist: contains all words in one list
    max_chars_per_row: max line length to justify to
    return: list of justified text rows
    """
    justified_text: list = []
    words_in_row: list = []
    chars_in_row: int = 0
    
    for word in wordlist:
        # fill a list with words until the word count is full
        if chars_in_row+len(word) <= max_chars_per_row:
            words_in_row.append(word)
            chars_in_row += len(word) + 1
        # word count for a row is full, now justify the row
        else:
            # justify a row
            justified_text.append(add_extra_separators(words_in_row, max_chars_per_row))
            words_in_row.clear()
            
            # .. and start filling a new row     
            words_in_row.append(word)
            chars_in_row = 0 + len(word) + 1               
    
    # add last row as a special case without justifcation
    last_row: str = ""
    for word in words_in_row:
        last_row += word + SEPARATOR
    
    last_row.rstrip()           
    justified_text.append(last_row) 
       
    return justified_text

def add_extra_separators(words_in_row: list, max_char_per_row: int) -> str:
    """
    Evenly distributes the amount of separators between two words.
    Adds "leftover" separators as +1 separator between first words,
    as long as they last.
    
    words_in_row: list of words in a row
    max_char_per_row: char limit of a row
    return: str, fully justified row
    """
    i: int = 0
 
    # if there is only one word in a row, don't justify it
    spaces_between_words = len(words_in_row)-1    
    if spaces_between_words == 0:        
        return words_in_row[0]
    
    # subtract total length of all words from the char limit
    amount_of_separators_required = max_char_per_row - sum(len(i) for i in words_in_row)       
  
    # how many separators is actually required for even spacing    
    n_separators = amount_of_separators_required // spaces_between_words
    # how many +1 leftover separators there are between words
    plus_one_separator_times = amount_of_separators_required % spaces_between_words
        
    justified_row = ""      

    # goes through the wordlist, adding words to string one by one
    while i <= spaces_between_words:
        justified_row += words_in_row[i]
        
        # adds n separators after added word for even spacing
        if i < spaces_between_words:
            justified_row += n_separators*SEPARATOR
            
            # adds a leftover separator after a word
            if plus_one_separator_times > 0:
                justified_row += SEPARATOR
                plus_one_separator_times -= 1 
            
        i += 1
       
    return justified_row

def main():
    # get input from user (text and row char limit)
    result = get_text()    
    justified_text = justify(result[0], result[1])
    
    # print the justified text
    for row in justified_text:
        print(row)

if __name__ == "__main__":
    main()