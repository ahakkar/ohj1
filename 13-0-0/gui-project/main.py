# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   26/10/2022, 22:19:18
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   

  Ohjelma toteuttaa Mastermind-pelin. Pelissä annetaan tai arvotaan
  ensin salainen 4-6 värin sarja. Sama väri voi esiintyä sarjassa
  useita kertoja, mutta mikään positiosta ei voi olla tyhjä.
  Käyttäjä yrittää arvata, mitkä värit esiintyvät sarjassa ja missä
  järjestyksessä. Tätä varten käyttäjä antaa oman 4-6 värin sarjansa,
  ja ohjelma ilmoittaa, kuinka monta väriarvausta meni täysin oikein
  (oikea väri oikeassa positiossa) sekä kuinka monta arvausta meni
  pelkästään värin osalta oikein (oikea väri väärässä positiossa).
  Tämän jälkeen käyttäjä voi tehdä uuden arvauksen jne.
    Aluksi käyttäjältä kysytään, täytetäänkö peliruudukko satunnaisesti
  arvottavilla väreillä vai käyttäjän luettelemilla väreillä.
  (Jälkimmäinen tapa ei ole kovin järkevä, mutta se on hyödyllinen
  testauksen kannalta.) Ensimmäisessä vaihtoehdossa käyttäjältä kysytään
  satunnaislukugeneraattorin siemenlukua ja jälkimmäisessä häntä
  pyydetään syöttämään n kpl värejä.
    Joka kierroksella käyttäjältä kysytään uutta arvausta. Peli päättyy
  pelaajan voittoon, jos arvaus menee jokaisen värin kohdalta täysin
  oikein. Peli päättyy pelaajan häviöön, jos hän ei ole arvannut oikein
  maksimimäärällä (10) arvauskertoja.
    Ohjelma tarkistaa, että annetut värit kuuluvat sallittujen värien
  joukkoon. Pelin päättyessä kerrotaan, voittiko vai hävisikö pelaaja.
'''

from mastermind import Ui

def main():
    ui = Ui()  
    ui.start()  

if __name__ == "__main__":
    main()
