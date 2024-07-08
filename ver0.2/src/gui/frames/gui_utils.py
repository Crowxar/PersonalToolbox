import tkinter as tk
import config as conf
import configparser
import os


config = configparser.ConfigParser()



def app_config():
    config.read(os.path.join(conf.appdata_path, 'config.ini'))
    configwidth = config.getint("Default Window Size", "width")
    configheight = config.getint("Default Window Size", "height")
    configposx = config.getint("Default Position", "x")
    configposy = config.getint("Default Position", "y")
    return configposy, configposx, configheight, configwidth

def basic_window():
    configposy, configposx, configheight, configwidth = app_config()
    
    root = tk.Tk()
    root.title("Blank Window")
    root.minsize(configwidth, configheight)
    root.geometry(f"{configwidth}x{configheight}+{configposx}+{configposy}")

    root.mainloop()