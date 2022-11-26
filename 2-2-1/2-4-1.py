"""
Eräässä pelissä pelaajat istuvat ringissä ja luettelevat jokainen vuorollaan lukuja siten, että pelin aloittaja sanoo luvun 1, hänen vieressään istuva luvun 2, ja seuraavaksi tulee tietenkin hänen vieressään istuva henkilö. Jotta peli ei olisi liian yksinkertainen, sanotaan kolmella jaollisten lukujen kohdalla "zip", seitsemällä jaollisten lukujen kohdalla "boing" ja sekä kolmella että seitsemällä jaollisten lukujen kohdalla "zip boing".

Toteuta ohjelma, joka tulostaa lunttilapun peliä pelaavalle jakolaskutaidottomalle henkilölle. Aluksi ohjelma kysyy, kuinka pitkälle lukuja tulostetaan.
"""
import math

def main():
    """
    sisältöä
    """
    user_input = int(input("How many numbers would you like to have? ")) + 1;

    for i in range(1, user_input):
        if (i % 3 == 0 and i % 7 == 0):
            print("zip boing")
        elif (i % 3 == 0):
            print("zip")
        elif (i % 7 == 0):
            print("boing")
        else:
            print(i)

        i += 1
   

if __name__ == "__main__":
    """
    sisältöä
    """
    main()