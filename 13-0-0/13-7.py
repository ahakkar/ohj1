# -*- encoding: utf-8 -*-
'''
@File    :   13-7.py
@Time    :   26/10/2022, 21:04:15
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   BMI CALC
'''

from tkinter import *

class Userinterface:

    def __init__(self):
        self.mw = Tk()
        self.mw.title("BMI calculator")
        self.mw.geometry("320x240")
        
        #constants
        self.ERROR_NUMBERS = "Error: height and weight must be numbers."
        self.ERROR_POSITIVE = "Error: height and weight must be positive."
        
        # variables
        self.texts:dict = {"norm": "Your weight is normal.",
                           "over": "You are overweight.",
                           "undr": "You are underweight."}       
        self.weight = 0
        self.height = 0
        self.BMI = 0        
        self.expl = "Input weight and height and\npress CALC to see BMI"        
        
        # row 0 GUI elements
        self.info_weight        = Label(self.mw, text="User wt in kg", borderwidth=1)
        self.__weight_value     = Entry()
        
        # row 1
        self.info_height        = Label(self.mw, text="User ht in cm", borderwidth=1)        
        self.__height_value     = Entry()
        
        # row 2
        self.__bmi_text         = Label(self.mw, text="BMI ->", borderwidth=1)
        self.__result_text      = Label(self.mw, text=str(self.BMI), borderwidth=1)
        
        # row 3
        self.__explanation_text = Label(self.mw, text=self.expl, borderwidth=1)
        
        # row 4
        self.__calculate_button = Button(self.mw, text="Calc", command=self.calculate_BMI)
        self.__stop_button      = Button(self.mw, text="Quit", command=self.stop)

        # placing GUI elements 
        self.info_weight.grid(row=0, column=0)        
        self.__weight_value.grid(row=0, column=1)
        
        self.info_height.grid(row=1, column=0)
        self.__height_value.grid(row=1, column=1)
        
        self.__bmi_text.grid(row=2, column=0)
        self.__result_text.grid(row=2, column=1)  
              
        self.__explanation_text.grid(row=3, columnspan=2)
        
        self.__calculate_button.grid(row=4, column=0)
        self.__stop_button.grid(row=4, column=1)
        
        

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Calculates  BMI and displays it, info about BMI, and error msgs
        """
        
        # must be numbers
        try:        
            self.weight = float(self.__weight_value.get())
            self.height = float(self.__height_value.get())/100
        except ValueError:
            self.__result_text.configure(text="")
            self.__explanation_text.configure(text=self.ERROR_NUMBERS)
            self.reset_fields()
            return
        
        # must be positive numbers
        if self.weight < 0 or self.height < 0:
            self.__result_text.configure(text="")
            self.__explanation_text.configure(text=self.ERROR_POSITIVE)
            self.reset_fields()
            return

        # calculate BMI and display it
        self.BMI = self.weight / pow(self.height, 2)
        self.__result_text.configure(text=f"{self.BMI:.2f}")
        
        # display info txt about BMI
        if self.BMI < 18.5:
            self.__explanation_text.configure(text=self.texts["undr"])
        elif self.BMI > 25:
            self.__explanation_text.configure(text=self.texts["over"])
        else:
            self.__explanation_text.configure(text=self.texts["norm"])

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)              

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.mw.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.mw.mainloop()

def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()

if __name__ == "__main__":
    main()
