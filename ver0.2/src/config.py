import configparser
import logging_config as log
import tkinter as tk
import utils as utils
import os

"""Functions related to the config.ini including defaults """

appdata_path = os.path.join(
        os.getenv('LOCALAPPDATA'),'PersonalToolkitAppdata')

def create_defaults():
    if not os.path.exists(os.path.join(appdata_path, 'config.ini')):
        os.makedirs(appdata_path, exist_ok=True)
        log.setup_logging(appdata_path)
        set_default_config(appdata_path)
        

def set_default_config(file_path):
    log.logging.info("Getting Screen Size")
    # Creating a tk instance and getting variables about screen size
    sizeroot = tk.Tk()
    screen_width, screen_height = (
        sizeroot.winfo_screenwidth(),
        sizeroot.winfo_screenheight(),)
    sizeroot.destroy()

    # Setting Config values starting with screen height/width
    config = configparser.ConfigParser()
    config["File Paths"] = {"config":file_path}

    config["Screen Size"] = {
        "width": int(screen_width),
        "height": int(screen_height)}
    
    # Setting default window size to 1/2 of the screen size
    default_width, default_height = screen_width // 2, screen_height // 2
    config["Default Window Size"] = {
        "width": str(default_width), "height": str(default_height)
        }

    # Setting default position to the center of the window
    default_x, default_y = default_width // 2, default_height // 2
    config["Default Position"] = {"x": str(default_x), "y": str(default_y)}

    #Writing the config file
    with open(os.path.join(file_path, "config.ini"), 'w') as configfile:
        log.logging.info("Writing config.ini")
        config.write(configfile)