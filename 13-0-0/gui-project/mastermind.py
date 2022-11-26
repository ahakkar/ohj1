# -*- encoding: utf-8 -*-
'''
@File    :   mastermind.py
@Time    :   27/10/2022, 16:27:08
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

from tkinter import *

class Ui:

    def __init__(self) -> None:
        self.mw = Tk()
        self.mw.title("Mastermind 1.0 © Antti Hakkarainen")
        self.set_window()
        self.set_menu()
        self.set_game_choices()
        self.set_game_board()  
                                    
        #constants
        
        #variables
                
        #gui elements
        #ask for colors
        #rand or set seed?
        # user guess?
        #render board
        # quit button
        
    def set_window(self):
        # adjust window size and center it to screen
        mw_width:int  = 480
        mw_height:int = 640
        screen_width = self.mw.winfo_screenwidth()
        screen_height = self.mw.winfo_screenheight()
        pos_x:int = int(screen_width / 2 - mw_width / 2)
        pos_y:int = int(screen_height / 2 - mw_height / 2)
        
        self.mw.geometry(f'{mw_width}x{mw_height}+{pos_x}+{pos_y}')                 
    
    def set_menu(self):
        self.menubar = Menu(self.mw)
        
        #file
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New game", command=self.donothing)
        self.filemenu.add_command(label="Restart game", command=self.donothing)
        self.filemenu.add_command(label="Scores", command=self.donothing)
        self.filemenu.add_command(label="Settings", command=self.donothing)
        self.filemenu.add_command(label="Exit", command=self.quit)
        
        #help
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Game rules", command=self.popup_help)
        self.helpmenu.add_command(label="About", command=self.popup_about)        
        
        #create menu
        self.menubar.add_cascade(label="File", menu=self.filemenu) 
        self.menubar.add_cascade(label="Help", menu=self.helpmenu) 
        self.mw.config(menu=self.menubar)
        
    def set_game_choices(self):
        gamemode = IntVar(self.mw, 1)     
        btn1 = Radiobutton(self.mw, text="Normal game", value=2, variable=gamemode)      
        btn2 = Radiobutton(self.mw, text="Predefined game", value=1, variable=gamemode)                         
        btn1.place(relx = 0.05, rely = 0.05, anchor = W)        
        btn2.place(relx = 0.05, rely = 0.1, anchor = W)           
        
        seed_text = Label(self.mw, text="Seed:")        
        seed_text.place(relx = 0.4, rely = 0.05, anchor = W)         
        seed = Entry() #enable when user selects predefined game
        seed.insert(END, "Random seed")
        seed.place(relx = 0.5, rely = 0.05, anchor = W) 
        
        start_game = Button(self.mw, text="Start game", width=15) 
        start_game.place(relx = 0.5, rely = 0.175, anchor = CENTER) 
        btn1.select()  
    
    def set_game_board(self):
        self.game_board = Canvas(self.mw, bg="white", height=480, width=440)
        
        STEP_BIG_CIRCLE = 75
        STEP_SMALL_CIRCLE = 30
        STEP_SMALL_CIRCLE_ROW2 = 25
        
        colors:list = ["red", "green", "yellow", "blue"]
        correct:list = ["black", "black", "black", "white"]
        
        # initial color line coordinates
        big_row_top = 25
        big_row_bot = 75
        big_x = 25
        big_y = 75
        
        # initial hint color coordinates
        small_x = 350
        small_row_top = 28
        small_y = 365        
        small_row_bot = 43        
        
        # render color line, move coords around while rendering
        for color in colors:
            self.game_board.create_oval(big_x, big_row_top, big_y, big_row_bot, fill=color)
            big_x += STEP_BIG_CIRCLE
            big_y += STEP_BIG_CIRCLE            
        
        # render hint colors, move coords around while rendering 
        i = 0    
        for color in correct:  
            # print row 2 below row 1  
            if i == 2:
                small_x -= STEP_SMALL_CIRCLE
                small_y -= STEP_SMALL_CIRCLE
                small_row_top += STEP_SMALL_CIRCLE_ROW2
                small_row_bot += STEP_SMALL_CIRCLE_ROW2       
            self.game_board.create_oval(small_x, small_row_top, 
                                        small_y, small_row_bot, fill=color)
            
            # move row 1 or row 2
            if i == 0 or i == 2:
                small_x += STEP_SMALL_CIRCLE
                small_y += STEP_SMALL_CIRCLE   
            i += 1            
       
        self.game_board.place(relx = 0.5, rely = 0.6, anchor = CENTER) 
        
    def donothing(self):
        self.filewin = Toplevel(self.mw)
        self.button = Button(self.filewin, text="Do nothing button")
        self.button.pack()
        
    def popup_about(self):
        # adjust window size and pos
        popup = Toplevel(self.mw)
        popup.title("About")
        
        popup_width:int = 320
        popup_height:int = 180  
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        pos_x:int = int(screen_width / 2 - popup_width / 2)
        pos_y:int = int(screen_height / 2 - popup_height / 2)
        popup.geometry(f'{popup_width}x{popup_height}+{pos_x}+{pos_y}')  
        #popup.geometry("320x240")
        #popup.anchor(anchor = CENTER)
        
        # contents
        about_text = Label(popup, text="" \
            + "Mastermind v. 1.0\n" \
            + "© Antti Hakkarainen\n\n" \
            + "Programmed for:\n" \
            + "COMP.CS.100 Ohjelmointi 1 in 2022")
                
        close = Button(popup, text="OK", width=15, command=popup.destroy)       
   
        # place buttons
        about_text.place(relx = 0.5, rely = 0.4, anchor = CENTER)  
        close.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
        # grab focus to about window     
        popup.focus()
        
    def popup_help(self):
        # adjust window size and pos
        popup = Toplevel(self.mw)
        popup.title("Game rules")
        
        popup_width:int = 440
        popup_height:int = 240  
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        pos_x:int = int(screen_width / 2 - popup_width / 2)
        pos_y:int = int(screen_height / 2 - popup_height / 2)
        popup.geometry(f'{popup_width}x{popup_height}+{pos_x}+{pos_y}')  
        #popup.geometry("320x240")
        #popup.anchor(anchor = CENTER)
        
        # contents
        help_text = "Yritä arvata, mitkä värit esiintyvät sarjassa ja missä " \
            + "järjestyksessä. Peli ilmoittaa, kuinka monta väriarvausta " \
            + "meni täysin oikein (MUSTA merkki: eli oikea väri oikeassa " \
            + "positiossa) sekä kuinka monta arvausta meni pelkästään värin " \
            + "osalta oikein (VALKOINEN merkki: oikea väri väärässä positiossa). " \
            + "Tämän jälkeen voit tehdä uuden arvauksen.\n\n" \
            + "Peli päättyy, kun arvaat kaikki värit oikein, tai 10 kierrosta on " \
            + "kulunut. Peli-iloa!"
        text = Label(popup, text=help_text, justify=LEFT, wraplength=360)
                
        close = Button(popup, text="OK", width=15, command=popup.destroy)       
   
        # place buttons
        text.place(relx = 0.5, rely = 0.4, anchor = CENTER)  
        close.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    
        # grab focus to about window     
        popup.focus()
                        
    def restart(self):
        """_summary_
        """
        
        self.mw.destroy()
        self.mw.mainloop()

    def quit(self):
        """
        Ends the execution of the program.
        """

        self.mw.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.mw.mainloop()