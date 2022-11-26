# -*- encoding: utf-8 -*-
'''
@File    :   7-9-0.py
@Time    :   21/10/2022, 21:20:19
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   Toteuta sanatiheyslaskuri,
             joka lukee käyttäjältä tekstipätkän ja tulostaa sitten tilaston
             eri sanojen esiintymistiheydestä kuten tässä esimerkkiajossa:
             
Example:

Enter rows of text for word counting. Empty row to quit.
I'm on a high way to hell
I'm on a high way to hell
It's going really well
Well it's only hell

a : 2 times
going : 1 times
hell : 3 times
high : 2 times
i'm : 2 times
it's : 2 times
on : 2 times
only : 1 times
really : 1 times
to : 2 times
way : 2 times
well : 2 times
'''



def main():
    result = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    
    while True:
        row = input()
        if len(row) > 0:
            items = row.split()
            # count the words in row and save data to dict
            for word in items:
                if not word.lower() in result:
                    result[word.lower()] = 1
                else:
                    result[word.lower()] +=1
        else:
            if len(result) > 0:
                # sort dict by key by saving key & value to new dict in sorted order
                abc = sorted(result)
                sorted_result = {}
                for key in abc:
                    sorted_result[key] = result[key]
                
                for key, val in sorted_result.items():
                    print(f"{key} : {val} times")
            return

if __name__ == "__main__":
    main()
