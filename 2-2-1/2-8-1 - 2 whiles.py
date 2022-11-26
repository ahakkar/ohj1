"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
2-8-1

Ei tätä kyllä pysty kahdella whilellä mitenkään tekemään :D
"""

def main():
    user_input = str

    while(True):
        user_input = input("Bored? (y/n) ")

        if user_input in ("y", "Y"):
            print(f"Well, let's stop this, then.")  
            break
        elif user_input in ("n", "N"):
            continue  
        else:
            print("Incorrect entry.")         

if __name__ == "__main__":
    main()