# -*- encoding: utf-8 -*-
'''
@File    :   12-4.py
@Time    :   26/10/2022, 17:47:22
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}

class Character:
    
    def __init__(self, name:str, hp:int):
        """
        param : TODO
        return: none
        """
        self.name:str = name
        self.hp:int = hp
        self.items:dict = {}        
        
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
        print("Hitpoints:", self.hp)
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
    
    def pass_item(self, item:str, target:type):
        """
        Transfers an item from char1 to char2     

        :param item: item to give to someone
        :param target: target of giving
        :return: bool, depending on success
        """

        if self.has_item(item):
            target.give_item(item)
            self.remove_item(item)
            return True
        return False
    
    def remove_hp(self, amt):
        """
        param : TODO
        return: none
        """
        
        self.hp -= amt
        
    def get_hp(self):
        """
        param : TODO
        return: none
        """
        
        return self.hp

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """
        
        if weapon not in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return False
        if not self.has_item(weapon):
            print(f"Attack fails: {self} doesn't have \"{weapon}\".")
            return False
        if target == self:
            print(f"Attack fails: {self} can't attack him/herself.")
            return False        
        
        target.remove_hp(WEAPONS[weapon])
        print(f"{self} attacks {target} delivering {WEAPONS[weapon]} damage.")
        if target.get_hp() < 1:
            print(f"{self} successfully defeats {target}.")
        return True
       

def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method
    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
