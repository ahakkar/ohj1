"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""

class Player:
    

        
    def __init__(self, name):
        """
        param : TODO
        return: none
        """
        
        self.__name__ = name
        self.__points__ = 0
        self.__won__ = False
        self.__throws__ = 0
        self.__all_throws__: list = []    
        
        
    def add_points(self, points):
        """
        param : TODO
        return: none
        """
        
        self.__throws__ += 1
        self.__all_throws__.append(points)     
        self.__points__ += points
                
        if self.__points__ > 50:
            print("Matti gets penalty points!")
            self.__points__ = 25
        elif self.__points__ == 50:
            self.__won__ = True
        elif self.__points__ >= 40:
            print(f"{self.__name__} needs only {50-self.__points__} points. It's better to avoid knocking down the pins with higher points.")
            
         # point out good throws
        if self.__throws__ > 1:
            if points > sum(self.__all_throws__)/self.__throws__:
                print(f"Cheers {self.__name__}!")  
            
    def get_hit_per(self):
        """
        param : TODO
        return: none
        """
        misses = 0     
        
        for throw in self.__all_throws__:
            if throw == 0:
                misses +=1
        
        if self.__throws__ < 1:
            return "hit percentage 0.0"
        
        return f"hit percentage {(1-misses/len(self.__all_throws__))*100:.1f}"
        
    def has_won(self):
        """
        param : TODO
        return: none
        """
        return self.__won__
    
    def get_name(self):
        """
        param : TODO
        return: none
        """
        return self.__name__
    
    def get_points(self):
        """
        param : TODO
        return: none
        """
        return self.__points__


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,", player1.get_hit_per())
        print(player2.get_name() + ":", player2.get_points(), "p,", player2.get_hit_per())
        print("")

        throw += 1


if __name__ == "__main__":
    main()
