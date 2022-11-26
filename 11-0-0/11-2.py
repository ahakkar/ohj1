# -*- encoding: utf-8 -*-
'''
@File    :   11-2.py
@Time    :   25/10/2022, 16:55:40
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
    
    def simplify2(self):
        """
        param : TODO
        return: none
        """
        
        div = greatest_common_divisor(self.__numerator, self.__denominator)
        result = f"{int(self.__numerator/div)}/{int(self.__denominator/div)}"
        return result
    
    def simplify(self):
        """
        param : TODO
        return: none
        """
        
        div = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator/div)
        self.__denominator = int(self.__denominator/div)
        

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    frac = Fraction(-2, -4)
    print(frac.return_string())
    print(frac.simplify())
    print('*'*20)
    
    frac = Fraction(37, 74)
    print(frac.return_string())
    print(frac.simplify())
    print('*'*20)
    frac = Fraction(-37, 74)
    print(frac.return_string())
    print(frac.simplify())
    print('*'*20)
        
    frac = Fraction(37, -74)
    print(frac.return_string())
    print(frac.simplify())
    print('*'*20)
    
if __name__ == "__main__":
    main()
