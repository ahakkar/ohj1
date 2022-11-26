# Paperi voittaa kiven, kivi voittaa sakset ja sakset voittavat paperin.

def rps(p1_input: str, p2_input: str):
    ''' kps-peli, vertailee 2 pelaajan arvoja ja kertoo voittajan'''
    winner = 0

    if p1_input == "R":
        if p2_input == "R":
            winner = 0
        elif p2_input == "P":
            winner = 2
        else:
            winner = 1

    elif p1_input == "P":
        if p2_input == "R":
            winner = 1
        elif p2_input == "P":
            winner = 0
        else:
            winner = 2

    elif p1_input == "S":
        if p2_input == "R":
            winner = 2
        elif p2_input == "P":
            winner = 1
        else:
            winner = 0

    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} won!")


def main():
    if True:
        p1_input = input("Player 1, enter your choice (R/P/S): ")
        p2_input = input("Player 2, enter your choice (R/P/S): ")
        rps(p1_input, p2_input)
    else:
        p1_input = "R"
        p2_input = "S"
        rps(p1_input, p2_input)

        p1_input = "R"
        p2_input = "R"
        rps(p1_input, p2_input)

        p1_input = "R"
        p2_input = "P"
        rps(p1_input, p2_input)

    

main()