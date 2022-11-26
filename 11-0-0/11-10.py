# -*- encoding: utf-8 -*-
'''
@File    :   11-10.py
@Time    :   26/10/2022 01:03:40
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

def menu(fracs:dict) -> None:   
    """PRints a menu

    :param dict fracs: empty dict to be used by menu
    """
    while True:
        cmd = str(input("> "))
        
        if cmd == "quit":
            print("Bye bye!")
            break
        
        elif cmd == "add":
            value = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")        
            parts = value.split('/')
            fracs[name] = Fraction(int(parts[0]), int(parts[1]))
            
        elif cmd == "print":
            name = input("Enter a name: ")
            if name in fracs:
                print(f"{name} = {fracs[name]}")
            else:
                print("Name x was not found")
                
        elif cmd == "list":
            if len(fracs) > 0:
                abc:list = sorted(fracs)
                for val in abc:
                    print(f"{val} = {fracs[val]}")
                
        elif cmd == "*":
            multiply_values(fracs)
                
        elif cmd == "file":
            fracs = read_file(fracs)
            
        else:
            print("Unknown command!")
            
def multiply_values(fracs:dict):
    """
    param : TODO
    return: none
    """
    
    a = input("1st operand: ")      
    if a not in fracs:        
        print(f"Name {a} was not found")
        return
    
    b = input("2nd operand: ")
    if not b in fracs:
        print(f"Name {b} was not found")
        return
    
    else:
        val1, val2 = fracs[a].return_values()
        orig = Fraction(val1, val2)
        val3, val4 = fracs[b].return_values()
        orig2 = Fraction(val3, val4)
        result = orig.multiply(orig2)
        
        print(f"{val1}/{val2} * {val3}/{val4} = {result}")
        print("simplified ", end ="")
        result.simplify()
        print(result)
            
def read_file(fracs:dict) -> dict:
    """
    param : TODO
    return: none
    """
    
    filename = input("Enter the name of the file: ")            
    try:
        with open(filename, mode="r") as read_file:
            data = read_file.readlines()
            read_file.close()
    except IOError:
        print("Error: the file cannot be read.")
        return fracs
    
    if len(data) > 0:
        for row in data:
            row = row.strip()
            items = row.split('=')
            
            try:
                if len(items) != 2 or len(items[0]) < 1:
                    print("Error: the file cannot be read.")
                    return fracs
                
                parts = items[1].split('/')
                if len(parts) != 2 or len(parts[0]) < 1 or len(parts[1]) < 1:
                    print("Error: the file cannot be read.")
                    return fracs           
            
                fracs[items[0]] = Fraction(int(parts[0]), int(parts[1]))
                
            except ValueError:
                print("Error: the file cannot be read.")
                return fracs
            except:
                continue
    else:
        print("Error: the file cannot be read.")
        return fracs
            
    return fracs
    
def main():
    
    fracs:dict = {}
    menu(fracs)     
    
       
if __name__ == "__main__":
    main()
