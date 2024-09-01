from tkinter import *

def TkLabel (window, text, x, y):
    Labels = Label(window, text=text, font=("Calibri", 12))
    Labels.place( x=x, y=y)
    
    return Labels

def TkMenuDropdown(window, val, OPTIONS, x, y):
    
    MenuDropdown = OptionMenu(window, val, *OPTIONS)
    MenuDropdown.place(x=x, y=y)
    
    return MenuDropdown