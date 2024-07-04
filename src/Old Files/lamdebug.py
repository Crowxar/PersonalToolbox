# lamdebug.py
import os
from ttkbootstrap import Style
from tkinter import ttk


# import lamdebug as DBG

# DBG.clear_terminal(RemoveToClear)
def clear_terminal(any=None):
    if any is None:
        os.system('cls')
        print('DBG - Program Cleared')


def button_test(name): # command=lambda: DBG.button_test(name)
    if name:
        print(f"DBG - {name.capitalize()} Button Pressed")
    else:
        print("DBG - Button Pressed")

def button_toggle_test(label_text):
    print(f"DBG - {label_text} toggled")


def setup_styles(): # DBG.setup_styles()
    style = Style()
    style.configure('DBGRED.TFrame', background='red')
    style.configure('DBGORA.TFrame', background='orange')
    style.configure('DBGYEL.TFrame', background='yellow')
    style.configure('DBGGRE.TFrame', background='green')
    style.configure('DBGBLU.TFrame', background='blue')
    style.configure('DBGPUR.TFrame', background='purple')

# region ========= lamdebug.py file ===== remove quotes =======
"""



# style='DBGStyleX.TFrame' where X is "" to 1-5
"""
# endregion