"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
3-6-1

Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a cow
E-I-E-I-O
With a moo moo here
And a moo moo there
Here a moo, there a moo
Everywhere a moo moo
Old MacDonald had a farm
E-I-E-I-O
---

Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a pig
E-I-E-I-O
With a oink oink here
And a oink oink there
Here a oink, there a oink
Everywhere a oink oink
Old MacDonald had a farm
E-I-E-I-O

Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a duck
E-I-E-I-O
With a quack quack here
And a quack quack there
Here a quack, there a quack
Everywhere a quack quack
Old MacDonald had a farm
E-I-E-I-O

Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a horse
E-I-E-I-O
With a neigh neigh here
And a neigh neigh there
Here a neigh, there a neigh
Everywhere a neigh neigh
Old MacDonald had a farm
E-I-E-I-O

Old MACDONALD had a farm
E-I-E-I-O
And on his farm he had a lamb
E-I-E-I-O
With a baa baa here
And a baa baa there
Here a baa, there a baa
Everywhere a baa baa
Old MacDonald had a farm
E-I-E-I-O
"""

def print_verse(animal: str, sound:str):
    """
    prints verses
    no return
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")



def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
