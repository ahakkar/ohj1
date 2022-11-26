"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.
        
        self.value = 0

        # TODO: Implement the rest of the needed methods here.
        self.mw = Tk()
        self.mw.geometry("600x400")
        
        self.__current_value_label = Label(self.mw, text=str(self.value), borderwidth=1)
        self.__current_value_label.pack(side=TOP)
        
        #buttons
        self.__reset_button = Button(self.mw, text="Reset", command=self.reset)
        self.__increase_button = Button(self.mw, text="Increase", command=self.increase)
        self.__decrease_button = Button(self.mw, text="Decrease", command=self.decrease)
        self.__quit_button = Button(self.mw, text="Quit", command=self.quit)
        self.__reset_button.pack(side=LEFT)
        self.__increase_button.pack(side=LEFT)
        self.__decrease_button.pack(side=LEFT)
        self.__quit_button.pack(side=LEFT)
        
        self.mw.mainloop()
        
    def reset(self):
        """
        param : TODO
        return: none
        """
        self.value = 0
        self.__current_value_label.configure(text=str(self.value))
        
    def increase(self):
        """
        param : TODO
        return: none
        """
        
        self.value += 1
        self.__current_value_label.configure(text=str(self.value))
    
    def decrease(self):
        """
        param : TODO
        return: none
        """
        
        self.value -= 1
        self.__current_value_label.configure(text=str(self.value))
        
    def quit(self):
        """
        param : TODO
        return: none
        """
        
        self.mw.destroy()

def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
