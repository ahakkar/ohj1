"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
4-14
"""
import math

def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car consume per hundred kilometers? ")
    x = y = float(0.0)
 
    while True:
        print(f"Coordinates x={x:.1f}, y={y:.1f}, the tank contains {gas:.1f} liters of gas.")
        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")

# Implement your own functions here. You are required to
# implement at least two functions that take at least
# one parameter and return at least one value.  The
# functions have to be used somewhere in the program.
def direction(cur_x, cur_y, dest_x, dest_y):
    """
    determine direction
    return direction x, y or xy
    """
    dir = str
    positive = True

    # move vertically
    if cur_x == dest_x:
        dir = "y"
        if 0 >= (dest_y - cur_y):
            positive = False

    # move horizontally
    elif cur_y == dest_y:
        dir = "x"
        if 0 >= (dest_x - cur_x):
            positive = False

    # move diagonally
    else:
        dir = "xy"

    #print("ajosuunta:", dir, positive)
    return dir, positive

def hypotenusa(a, b):
    """
    calculates hypotenusa from 2 straight sides (a,b) of triangle
    returns hypotenusa
    """
    c = math.sqrt(pow(a, 2)+pow(b, 2))
    return c

def fill(tank_size: float, to_fill: float, gas: float):
    """
    tank_size:   the size of the tank
    to_fill:     the amount of gas that is requested to be filled in
    gas:         the amount of gas in the tank currently
    """
    if (to_fill + gas > tank_size):
        return tank_size
    else:
        return to_fill + gas

def drive(cur_x: float, cur_y: float, dest_x: float, dest_y: float, gas: float, gas_consumption: float):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate  
    """

    final_x = final_y = float   # how far we get actually
    max_dist = (gas/gas_consumption)*100
    rem_gas = float
    pos = bool

    # determine direction, and if movement is positive or negative in xy coords
    dir, pos = direction(cur_x, cur_y, dest_x, dest_y)

    # car moves horizontally
    if dir == "x":
        distance = abs(dest_x - cur_x)
        gas_used = (gas_consumption/100)*distance        

        #bensaa meni liikaa
        if gas_used > gas:            
            rem_gas = 0
            if pos:
                final_x = cur_x+max_dist
            else:
                final_x = cur_x-max_dist
            final_y = cur_y
        else:
            rem_gas = gas-gas_used
            final_x = dest_x
            final_y = cur_y

    # car moves vertically
    elif dir == "y":
        distance = abs(dest_y - cur_y)
        gas_used = (gas_consumption/100)*distance

        #bensaa meni liikaa
        if gas_used > gas:            
            rem_gas = 0
            final_x = cur_x            
            if pos:
                final_y = cur_y+max_dist
            else:
                final_y = cur_y-max_dist
        else:
            rem_gas = gas-gas_used
            final_x = cur_x
            final_y = dest_y

    # car moves diagonally
    elif dir == "xy":
        distance = abs(hypotenusa((dest_x - cur_x), (dest_y - cur_y)))
        gas_used = (gas_consumption/100)*distance

        #bensaa meni liikaa
        if gas_used > gas:            
            rem_gas = 0
            percentage = max_dist/distance
            final_x = dest_x*percentage
            final_y = dest_y*percentage
        else:
            rem_gas = gas-gas_used
            final_x = dest_x
            final_y = dest_y
    else:
        print("Nyt meni jotain pieleen, väärä suunta!")

    return rem_gas, final_x, final_y  


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """
    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    """
    """
    menu()

if __name__ == "__main__":
    main()