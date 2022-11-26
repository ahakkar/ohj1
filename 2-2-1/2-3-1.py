"""
Tee ohjelma, joka tulostaa annetun luvun kertotaulun koulutyyliin kertoimilla yhdestä kymmeneen.

Esimerkki ohjelman toiminnasta:

Choose a number: 6
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
...
10 * 6 = 60
"""

def main():
    """
    sisältöä
    """
    user_input = int(input("Choose a number: "))      

    for i in range(1,11):
        print(f"{i} * {user_input} = {i*user_input}")
        i += 1

if __name__ == "__main__":
    """
    sisältöä
    """
    main()