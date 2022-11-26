"""
antti.i.hakkarainen@tuni.fi

"""

def main():
    user_input = str

    #  or user_input != "Y" or user_input != "n" or user_input != "N" */

    while(True):
        accepted_answers = ["y", "Y"]
        quit_program = False
        user_input = input("Bored? (y/n) ")        

        for val in accepted_answers:
            if user_input == val:
                quit_program = True
                break

        if user_input == "n" or user_input == "N":
            continue   
        elif quit_program:
            print(f"Well, let's stop this, then.")  
            break
        else:
            print("Incorrect entry.")         

if __name__ == "__main__":
    main()