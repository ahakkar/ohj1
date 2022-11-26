"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
"""

class Car:
    """
    Class Car: Implements a car
    """

    def __init__(self, tank_size, gas_consumption):
        """
        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0.0
        self.__odometer = 0.0


    # TODO:
    # Add the definitions of all methods of this class here.
    # The methods are a part of the class. Therefore, they are intended on
    # this level (i.e. inside the class definition).

    # When printing the car status, use the following f-string to make
    # sure the printout is in the correct format to pass the automated tests:
    #
    #    f"The tank contains {:.1f} liters of gas and the odometer shows {:.1f} kilometers."
    #                         ^                                           ^
    #
    # You need to add the correct attributes to points marked with carets "^".
    
    def fill_tank(self, amount):
        """
        param : TODO
        return: none
        """
        if amount < 0:
            print("You cannot remove gas from the tank")
            return
        
        if amount < self.__tank_volume - self.__gas:
            self.__gas += amount
        else:
            self.__gas = self.__tank_volume 

    def drive_distance(self, distance):
        """
        param : TODO
        return: none
        """
        rem_gas:float = self.__gas
        
        gas_used = (self.__consumption/100)*distance  
        if gas_used > self.__gas:
            rem_gas = 0
            self.__odometer += self.__gas/self.__consumption*100
        else:
            rem_gas = self.__gas - gas_used
            self.__odometer += gas_used/self.__consumption*100
            
        self.__gas = rem_gas
        
    def print_information(self):
        """
        param : TODO
        return: none
        """
        
        print(f"The tank contains {self.__gas:.1f} liters of gas and the odometer shows {self.__odometer:.1f} kilometers.")

def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)
    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            car.fill_tank(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            
            car.drive_distance(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
