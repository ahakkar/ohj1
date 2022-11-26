"""
Tee ohjelma, joka kysyy käyttäjältä onko tylsää, kunnes käyttäjällä on tylsää. Esimerkkejä ohjelman toiminnasta:

Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) y
Well, let's stop this, then.
"""

def main():
    """
    Tee ohjelma, joka kysyy käyttäjältä onko tylsää, kunnes käyttäjällä on tylsää. Esimerkkejä ohjelman toiminnasta:

    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) y
    Well, let's stop this, then.
    """
    user_input = str

    while(True):
        user_input = input("Bored? (y/n) ")
        if(user_input == "n"):
            print("Well, let's stop this, then.")
            break

if __name__ == "__main__":
    """
    Tee ohjelma, joka kysyy käyttäjältä onko tylsää, kunnes käyttäjällä on tylsää. Esimerkkejä ohjelman toiminnasta:

    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) n
    Bored? (y/n) y
    Well, let's stop this, then.
    """
    main()