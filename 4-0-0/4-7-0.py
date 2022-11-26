"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
4-6-1
"""

def factorial(number: int):
    """    
    calculates factorial
    returns factorial
    """
    n = i = 1
    
    while (i <= number):
        n = n * i
        i += 1

    return n;


def calc_probability(total_balls:int, drawn_balls:int):
    """    
    calculates prob with balls
    return probability

    calculate probability, formula:
                n!
    -----------------------
    (total-drawn)! * drawn!
    """
    probability = float
    probability = factorial(total_balls)/(factorial((total_balls-drawn_balls)) * factorial(drawn_balls))

    return probability

def check_input(total_balls:int, drawn_balls:int):
    """
    user input error checking
    """
    if (total_balls < 1 or drawn_balls < 1):
        print("The number of balls must be a positive number.")
        return False
    elif (drawn_balls > total_balls):
        print("At most the total number of balls can be drawn.")
        return False
    
    return True

def main():
    valid_input = bool
    total_balls = drawn_balls = int
    probability = float

    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    valid_input = check_input(total_balls, drawn_balls)
    if(valid_input):
        probability = calc_probability(total_balls, drawn_balls);
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{probability:.0f}")  
 

if __name__ == "__main__":
    main()