"""
antti.i.hakkarainen@tuni.fi

tulostelee päiviä
"""

def main():
    MONTHS = 12;

    for month in range(1, MONTHS+1):
        total_days = 31 #oletus
        [2,4,6,9,11]

        if month == 2:
            total_days = 28
        if month in [4,6,9,11]:
            total_days = 30

        for day in range(1, total_days+1):
            print(f"{day}.{month}.")


if __name__ == "__main__":
    main()