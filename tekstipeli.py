
def menu():
    """
    """
    turn = 1

    while True:        

        if (turn == 1):
            print("Welcome.")
        elif (turn == 2):
            print("You have a sudden feeling that you are not alone.")
        elif (turn == 3):
            which = choose_randomly(["left", "right"])
            print(f"You hear some quiet noises from your {which} side.")
            print("You can't quite figure out what could be the source of it.\n")
        elif (turn == 4):
            print("A black shape appears from the darkness. You raise your sword")
            print("as a precaution.\n")
        else:
            battle()
            break

        choice = input("1) Look 2) Examine 3) Wait q) Quit\n-> ")

        if choice == "1":
            look_around(turn)
        elif choice == "2":          
            examine()
        elif choice == "3":
            turn += 1
            continue
        elif choice == "q":
            break

        turn += 1

    print("Thank you for playing the game!")

def look_around(turn):
    if (turn < 3):
        print("You seem to stand on a smoothly polished obisidan stone. The floor")
        print("continues into darkness. You feel that staying still for a while")
        print("is the best choice for now.\n")
    elif (turn < 4):
        print("The darkness surrounding you seems to draw in closer, tighter. The")
        print("surface of the darkness is misty, undulating, pulsating. It ebbs and")
        print("flows ever closer and closer...\n")
    elif (turn == 4):
        print("You really can't make out the exact features of the shape, especially")
        print("not in this enroaching darkness. It looks like a human-sized creature")
        print("which is holding a inky dark sword with a bright, sharp-looking")
        print("edge. From your experience people don't approach each other a sword")
        print("in hand if their intentions are peaceful. You get mentally ready for")
        print("combat.\n")
    else:
        print("[You should not be here.]")


def battle():
    hitpoints = 2
    turn = 1
  
    while True:
        if (turn == 1):
            print("A battle ensues.\n")
            print("The shape looks like it is going to lunge straight at your chest.")
            print("What will you do? \n")
        elif (turn == 2):
            if (hitpoints == 1):
                print("Make haste. The wound does not feel good, so you probably have")
                print("time only for a direct attack.\n")
            else:
                print("You both stand ready.")
        elif (turn == 3 or turn == 4):
            print("The world somehow does not feel as stable and substantial as it should.")
            print("You both stand ready.")
        elif (turn == 5):
            print("The world starts to dissolve around you. Blackness fades through gray")
            print("to white. You wake up from the nightmare.")
            break
        else:
            print("You should be dead already!")
            break

        choice = input("1) Lunge 2) Parry 3) Wait 4) Dodge\n-> ")

        if choice == "1":
            if (turn == 1):
                hitpoints = 1
                print("You both lunge at the same time. The shape skillfully")
                print("dodges your sword, but manages to scrape your unprotected thigh")
                print("with its dark sword. You feel blood instantly wetting your trousers.")
                print("This is not a good situation.\n")
            else:
                if (hitpoints == 1):
                    print("Despite your wounds, you make a concentrated strike towards the")
                    print("location where you assume the enemy will be. You drastically mis-")
                    print("judge the actions, but somehow end up effortlessly severing")
                    print("the head off of the shape.")
                    print("")
                    print("You hastily start to bandage your wound.. and wake up from the dream.")
                    break
                else:
                    print("You estimate your strike well, and manage to dodge the incoming")
                    print("attack, while striking the enemy straight to the presumed heart.")
                    print("")
                    print("You wake up from the dream.")
                    break

        elif choice == "2":          
            if (hitpoints == 2):
                print("You skillfully parry the strike, but have no time for a countermove.\n")
            else:
                hitpoints = 0
                print("You are slowed by your wounds. You lethargically try to parry the")
                print("attack but fail. The sword pierces through your armor.\n")                

        elif choice == "3":
            hitpoints = 0
            print("The pointed end of the dark sword cleanly pierces through your")
            print("chainmail and your chest. The world fades around you to complete")
            print("darkness.\n") 

        elif choice == "4":
            if (hitpoints == 2):
                print("You skillfully dodge the strike, but have no time for a countermove.\n")
            else:
                hitpoints = 0
                print("You are slowed by your wounds. Your attempt at dodging the attack")
                print("is futile. The sword cleanly pierces through your armor.\n")

        else: 
            print("[You should not be here.]")

        if (hitpoints == 0):
            print("You die.")
            break

        turn += 1

def choose_randomly(options: list):
    from random import choice
    return choice(options)

def examine():
    examined = 0

    while True:        
        if (examined == 0):
            print("What would you like to examine?")
        else:
            print("Would you like to examine something else?")

        choice = input("1) Your sword 2) Your armor r) return\n-> ")
        if choice == "1":
            render_graphics("sword")
            print("You seem to own a very fine and sharp longsword. You have a feeling that " + 
                "you are probably quite experienced at using it.\n")
        elif choice == "2":          
            print("Your armor seems to be of a good quality, made by an experienced blacksmith.")
            print("The armor is made of small metal rings linked together in a pattern to form a mesh.")
            print("Some people would call this a chain mail. The steel is slightly oiled to keep the")
            print("rust away. You have a feeling that it will provide a reasonable amount of")
            print("protection against common foes.")
            print()
        elif choice == "r":
            return None   

        examined += 1

def render_graphics(graphic: str):
    if (graphic == "sword"):
        print("             <>")
        print("            //")
        print("           //")
        print("C>(((((((({@}::::::::::::::::::::::::::::::::::::::::::::::::::::======-")
        print("           \\\\")
        print("            \\\\")
        print("             <>\n")
    
        

def read_number(prompt, error_message="Incorrect input!"):
    """
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