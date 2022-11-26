"""
Kirjoita ohjelma, joka kysyy ostosten hinnan ja millä rahalla maksetaan ja tulostaa, 
minkälaisia vaihtorahoja pitää antaa. Yksinkertaistetaan ohjelmaa niin, että käytössä
 ei ole kuin 1, 2, 5 ja 10 euron rahoja ja kokonaishinta on aina tasaeuroja.

Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins
"""

def change(price: int, money: int):
    '''price = tuotteiden hinta
        money = asiakkaalta saatu saatu raha
        
        tulostus: vaihtorahat'''
    change_amt = money-price
    if change_amt > 0:
        coins = {"ten-euro notes": 10, "five-euro notes": 5, "two-euro coins": 2, "one-euro coins": 1}
        print("Offer change:")
        for coin in coins:
            if change_amt // coin > 0
        if change_amt // 10 > 0:
            print(f"{change_amt // 10} ten-euro notes")
            change_amt -= (change_amt // 10)*10
        
        if change_amt // 5 > 0:
            print(f"{change_amt // 5} five-euro notes")
            change_amt -= (change_amt // 5)*5
        
        if change_amt // 2 > 0:
            print(f"{change_amt // 2} two-euro coins")
            change_amt -= (change_amt // 2)*2

        if change_amt // 1 > 0:
            print(f"{change_amt // 1} one-euro coins")
            change_amt -= (change_amt // 1)*1
    else:
        print("No change")

def main():
    if True:
        price = int(input("Purchase price: "))
        money = int(input("Paid amount of money: "))

        change(price, money)
    else:
        change(12,50)
        change(24,50)
        change(50,12)
        change(12,12)

main()