# -*- encoding: utf-8 -*-
'''
@File    :   11-4.py
@Time    :   25/10/2022, 17:14:40
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
    
    """
    Magical Comparison Operators	Description
    __lt__	describes less than operator(<)
    __le__	descries less than or equal to (<=)
    __gt__	describes greater than (>)
    __ge__	describes greater than or equal to (>=)
    __eq__	describes equality operator(==)
    __ne__	describes not equal to operator(!=)
    """
    
    def __str__(self):
        """
        param : TODO
        return: none
        """
        
        return self.return_string()
    
    def __lt__(self, obj2):
        """
        param : TODO
        return: none
        """
        
        values = obj2.return_values()
        
        a:float = self.__numerator/self.__denominator
        b:float = values[0]/values[1]
        
        if a < b:
            return True
        return False        
    
    def __gt__(self, obj2):
        """
        param : TODO
        return: none
        """
        
        values = obj2.return_values()
        
        a:float = self.__numerator/self.__denominator
        b:float = values[0]/values[1]
        
        if a > b:
            return True
        return False     

    def __init__(self:type, numerator:int, denominator:int):
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
        
    def return_values(self:type) -> tuple:
        """
        param : TODO
        return: none
        """
        
        return (self.__numerator, self.__denominator)

    def return_string(self:type):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
    
    def simplify(self:type):
        """
        param : TODO
        return: none
        """
        
        div = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator/div)
        self.__denominator = int(self.__denominator/div)
        
    def complement(self:type) -> type:
        """
        param : TODO
        return: none
        """
        
        if self.__numerator > 0:
            self.__numerator -= abs(self.__numerator*2) 
        elif self.__denominator > 0:                   
            self.__denominator -= abs(self.__denominator*2)      
            
        return self
        
    def reciprocal(self:type) -> type:
        """
        param : TODO
        return: none
        """
        
        temp = self.__denominator
        self.__denominator = self.__numerator
        self.__numerator = temp
        
        return self
    
    def multiply(self:type, Num1:type) -> type:
        """
        param : TODO
        return: none
        """
        
        values = Num1.return_values()
        
        num = self.__numerator * values[0]
        denom = self.__denominator * values[1]     
        
        self.__numerator = num
        self.__denominator = denom
        
        return self
    
    def divide(self:type, Num1:type) -> type:
        """
        param : TODO
        return: none
        """
                       
        return self.multiply(Num1.reciprocal())
    
    def add(self, Num1) -> type:
        """
        param : TODO
        return: none
        """
        
        values = Num1.return_values() 
        
        a = self.__numerator * values[1]
        b = self.__denominator * values[1]
        c = values[0] * self.__denominator
                    
        num = a+c
        denom = b
        
        self.__numerator = num
        self.__denominator = denom
        return self
    
    def deduct(self:type, Num1:type) -> type:
        """
        param : TODO
        return: none
        """
        
        values = Num1.return_values() 
        
        a = self.__numerator * values[1]
        b = self.__denominator * values[1]
        c = values[0] * self.__denominator
                    
        num = a-c
        denom = b
        
        self.__numerator = num
        self.__denominator = denom
        return self

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
    
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    print("True?", frac1 < frac2)
    
    print("False?", frac1 > frac2)
    

    """
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)
    sum = frac1.add(frac2)
    print('15/18?', sum.return_string())
    
    sum.simplify()
    print('5/6?', sum.return_string())
    
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)
    difference = frac1.deduct(frac2)
    print('9/18?', difference.return_string())
    
    difference.simplify()
    print('1/2?', difference.return_string())
    
    
    frac1 = Fraction(4, 8)
    frac2 = Fraction(2, 1)
    quotient = frac1.divide(frac2)
    print("4/16?", quotient.return_string())
    
    quotient.simplify()
    print("1/4?", quotient.return_string())

    
    object1 = Fraction(2, 3)
    object2 = Fraction(4, 5)
    result = object1.multiply(object2)
    print(result.return_string())
    
    frac = Fraction(2, 4)
    complement = frac.complement()
    print("2/4 is:", complement.return_string(), "complement should: -2/4") 
    print('*'*20)
    
    frac = Fraction(2, -4)
    complement = frac.complement()
    print("2/-4 is:", complement.return_string(), "complement should: 2/4") 
    print('*'*20)
    """
    
   
   
if __name__ == "__main__":
    main()
