"""
Tee ohjelma, joka tulostaa annetun luvun kertotaulua niin kauan, että päästään tulokseen, joka on suurempi kuin sata.

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
17 * 6 = 102
"""
import math

def main():
    """
    sisältöä
    """
    user_input = int(input("Choose a number: "))  
    times_to_multiply = math.ceil(100/user_input) + 1
    

    for i in range(1,times_to_multiply):
        print(f"{i} * {user_input} = {i*user_input}")
        i += 1

if __name__ == "__main__":
    """
    sisältöä
    """
    main()