"""
Edellisessä kohdassa toteutettu ohjelma toimii hiukan hölmösti, jos syötetään
 jotain muuta kuin "y", "Y", "n" tai "N". Toteutetaan nyt kokonaan uuteen 
 ohjelmaan pelkästään toistorakenne, joka kysyy käyttäjän vastausta uudelleen,
  mikäli käyttäjä vastaa jotain muuta kuin "y", "Y", "n" tai "N".
"""

def main():
    """
    sisältöä
    Incorrect entry.
    """
    user_input = str

    #  or user_input != "Y" or user_input != "n" or user_input != "N" */

    while(True):
        accepted_answers = ["y", "Y", "n", "N"]
        correct_answer = False
        user_input = input("Answer Y or N: ")        

        for val in accepted_answers:
            if user_input == val:
                correct_answer = True
                break

        if correct_answer:
            print(f"You answered {user_input}")
            break
        else:
            print("Incorrect entry.")         

if __name__ == "__main__":
    """
    sisältöä
    """
    main()