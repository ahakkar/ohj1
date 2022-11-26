"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
4-6-1
"""

def compare_floats (num1: float, num2: float, eps: float):
    """
    Toteuta funktio compare_floats, joka ottaa parametrinaan kaksi liukulukua sekä
    vertailussa käytettävän epsilonin arvon ja palauttaa totuusarvona tiedon,
    ovatko luvut samoja annetun epsilonin tarkkuudella vertailtuna.
    """

    close = abs(num1 - num2) < eps

    if close:
        return True
    else:
        return False

def main():
    EPSILON = 0.000000001
    compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON)
    compare_floats(0.0002, 0.0000002, EPSILON)
    

if __name__ == "__main__":
    main()