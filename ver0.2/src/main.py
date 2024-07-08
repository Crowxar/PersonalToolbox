import utils
import config as con
import logging_config as log
import os
from gui.frames import gui_utils

def main():
    """
    This function is the entry point of the program. Will start by creating
    config files in localappdata and then launch the GUI.
    """

    con.create_defaults()
    gui_utils.basic_window()
    
if __name__ == "__main__":
    main()
