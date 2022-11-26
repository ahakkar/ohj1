"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
3-6-2

I know someone you don't know
Yogi, Yogi
I know someone you don't know
Yogi, Yogi Bear
Yogi, Yogi Bear
Yogi, Yogi Bear
I know someone you don't know
Yogi, Yogi Bear

Yogi has a best friend too
Boo Boo, Boo Boo
Yogi has a best friend too
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Yogi has a best friend too
Boo Boo, Boo Boo Bear

Yogi has a sweet girlfriend
Cindy, Cindy
Yogi has a sweet girlfriend
Cindy, Cindy Bear
Cindy, Cindy Bear
Cindy, Cindy Bear
Yogi has a sweet girlfriend
Cindy, Cindy Bear
"""

def repeat_name(name:str, times:int):
    """
    prints bears
    return none
    """
    i = 1
    while i <= times:
        print(f"{name}, {name} Bear")
        i += 1
    
def verse(verse:str, name:str):
    """
    prints verses
    no return value
    """
    print(verse)
    print(f"{name}, {name}")
    print(verse)
    repeat_name(name, 3)
    print(verse)
    repeat_name(name, 1)

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
