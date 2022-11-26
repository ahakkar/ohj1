"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def input_from_user(q:str):
    """
    kysyy kysymyksen ja lukee inputin
    palauttaa inputin
    """
    return int(input(q))

def calculate_dose(wt: int, time: int, prev: int):
    """
    Toteuta funktio calculate_dose, joka laskee ja palauttaa oikean annoksen, 
    kun sille annetaan parametreina tarvittavat lähtöarvot seuraavassa järjestyksessä:
    potilaan paino, aika edellisen annoksen saamisesta, aiempi vuorokausiannos
    (siis viimeisen 24 tunnin aikana nautittu annos).

    15mg/kg/6h
    """

    dose = 0
    dose_in_6h = 15*wt
    remaining_dose_in_24h = 4000-prev

    if prev >= 4000 or time < 6:
        return dose
    elif remaining_dose_in_24h > dose_in_6h:
        return dose_in_6h
    else:
        return remaining_dose_in_24h
    


def main():
    wt = input_from_user("Patient's weight (kg): ")
    time = input_from_user("How much time has passed from the previous dose (full hours): ")
    prev = input_from_user("The total dose for the last 24 hours (mg): ")
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(wt, time, prev)}")

if __name__ == "__main__":
  main()
