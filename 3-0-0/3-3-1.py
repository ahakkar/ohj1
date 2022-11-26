"""
COMP.CS.100 Ohjelmointi 1.
Antti Hakkarainen, antti.i.hakkarainen@tuni.fi, opiskelijanumero K79735.
3-3-1 Ohjelma, joka vertailee inflaatiolukuja keskenään ja tulostaa suurimman nousun

Aloitettu 16:07
Valmis 16:44
"""

def main():
    month = 1
    prev_month = False      # for first month handling
    monthly_changes = []    # collect list of all monthly charges, sort them and print out largest change
    largest_change = float

    # ask input from user until input is empty (user presses enter)
    while True:
        user_input = input(f"Enter inflation rate for month {month}: ")

        # program logic
        if user_input != "":
            # handle first month input
            if not prev_month:
                prev_month = float(user_input)            
            else:
                monthly_changes.append(float(user_input)-prev_month)         

            # test print      
            # print(f"prev: {prev_month}, input: {user_input}, change: {largest_change:.1f}")
            prev_month = float(user_input)

        # errors, exiting program
        if month <= 2 and user_input == "":
            print("Error: at least 2 monthly inflation rates must be entered.")
            break 
        
        # sorts from small to largest list item
        # -1 picks last item from list, which is largest
        elif month >= 2 and user_input == "":
            monthly_changes.sort()  
            largest_change = f"{monthly_changes[-1]:.1f}" 
            print(f"Maximum inflation rate change was {largest_change} points.")
            break

        month += 1

if __name__ == "__main__":
    main()