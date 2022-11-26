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

    # move vertically
    if cur_x == dest_x:
        dir = "y"

    # move horizontally
    elif cur_y == dest_y:
        dir = "x"

    # move diagonally
    else:
        dir = "xy"

    print("travel direction:", dir)
    return dir

def func2(value):
    """
    """
    return None

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

        The return values have to be in this order.
        The function does not print anything and does not ask for any
        input.
    """

    final_x = final_y = float   # how far we get actually
    max_dist = (gas/gas_consumption)*100
    rem_gas = float

    #print(f"{cur_x}, {cur_y}, {dest_x}, {dest_y}")
    #print("polttoaineen määrä ja kulutus", gas, gas_consumption)

    dir = direction(cur_x, cur_y, dest_x, dest_y)
    #print(f"dir {dir}")

    if dir == "x":
        distance = dest_x - cur_x
        gas_used = (gas_consumption/100)*distance
        #print("matka, kulutus", distance, gas_used)

        if gas_used > gas:
            #bensaa meni liikaa
            rem_gas = 0
            final_x = cur_x+max_dist
            final_y = cur_y
        else:
            rem_gas = gas-gas_used
            final_x = dest_x
            final_y = cur_y

    elif dir == "y":
        distance = dest_y - cur_y
        gas_used = (gas_consumption/100)*distance
        #print("matka, kulutus", distance, gas_used)

        if gas_used > gas:
            #bensaa meni liikaa
            rem_gas = 0
            final_x = cur_x
            final_y = cur_y+max_dist
        else:
            rem_gas = gas-gas_used
            final_x = cur_x
            final_y = dest_y

    elif dir == "xy":
        distance = math.sqrt(
            pow((dest_x - cur_x), 2) +
            pow((dest_y - cur_y), 2)
            )
        #print("pythagoras", distance)
        gas_used = (gas_consumption/100)*distance
        #print("matka, kulutus", distance, gas_used)

        if gas_used > gas:
            #bensaa meni liikaa
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
    print()
    print("matka 1, suunta x", drive(0.0, 0.0, 5.0, 0.0, 32, 5.0))
    print()
    print("matka 2, suunta x, tankki ei riitä", drive(0.0, 0.0, 5.0, 0.0, 23, 5.0))
    print()
    print("matka 3, suunta y", drive(0.0, 0.0, 0.0, 6.0, 32, 5.0))
    print()
    print("matka 4, suunta y, tankki ei riitä", drive(0.0, 0.0, 0.0, 5.0, 23, 5.0))
    
    print()
    print("matka 5, suunta xy", drive(200.0, 200.0, 400.0, 300.0, 32, 5.0))
    print()
    print("matka 6, suunta xy, tankki ei riitä", drive(200.0, 200.0, 400.0, 300.0, 6, 5.0))
    """
    menu()

if __name__ == "__main__":
    main()