from tkinter import *

class Käyttöliittymä:
  def __init__(self):
    self.__pääikkuna = Tk()

    self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!")
    self.__tekstikenttä.pack()

    self.__pääikkuna.mainloop()

def main():
  käli = Käyttöliittymä()

if __name__ == "__main__":
    main()