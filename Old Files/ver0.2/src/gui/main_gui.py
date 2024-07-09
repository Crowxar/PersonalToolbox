import configparser
import frames
import tkinter as tk

"""
Logic to handle the overall GUI - sub sections will be broken down to their
individual files within the gui folder
"""



config_file_location = r"ver0.2\output\config.ini"
config = configparser.ConfigParser()


def show_frame(frame):
    # Hide all frames except the current one
    for f in (frames.home_gui):
        f.pack_forget()
    # Show the selected frame
    frame.pack(fill="both", expand=True)






