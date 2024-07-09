import config as con
from gui import main_gui

def main():
    """
    This function is the entry point of the program. Will start by creating
    config files in localappdata and then launch the GUI.
    """

    #con.create_defaults()
    main_gui.main_window()
    

if __name__ == "__main__":
    main()