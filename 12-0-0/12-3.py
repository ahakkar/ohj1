"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    
    def __init__(self, name:str):
        """
        param : TODO
        return: none
        """
        self.name = ""
        self.items = {}
        self.name = name
        
    def __str__(self):
        """
        param : TODO
        return: none
        """
        
        return self.name
    
    def printout(self):
        """
        param : TODO
        return: none
        """
        
        print("Name:", self.name)
        if len(self.items) > 0:
            abc:list = sorted(self.items)
            
            for item in abc:
                print(f"  {self.items[item]} {item}")
        else:
            print("  --nothing--")
        
    def give_item(self, item:str):
        """
        param : TODO
        return: none
        """
        
        if item in self.items:
            self.items[item] +=1
        else:
            self.items[item] = 1
            
    def remove_item(self, item:str):
        """
        param : TODO
        return: none
        """
        
        if item in self.items:
            if self.items[item] > 1:
               self.items[item] -= 1
            else:
                self.items.pop(item)
                
    def get_name(self):
        """
        param : TODO
        return: none
        """
        
        return self.name 
    
    def has_item(self, item:str):
        """
        param : TODO
        return: none
        """
        
        if item in self.items:
            return True
        return False
    
    def how_many(self, item:str):
        """
        param : TODO
        return: none
        """
        if item in self.items:
            return self.items[item]
        return 0

def main():
    character1 = Character("Conan the Barbarian")    
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
