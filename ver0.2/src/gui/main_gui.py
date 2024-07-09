import tkinter as tk
import gui.home_gui
import gui.schedule_gui
import configparser
import os
import config as conf

def app_config():
    config = configparser.ConfigParser()
    config.read(os.path.join(conf.appdata_path, 'config.ini'))
    configwidth = config.getint("Default Window Size", "width")
    configheight = config.getint("Default Window Size", "height")
    configposx = config.getint("Default Position", "x")
    configposy = config.getint("Default Position", "y")
    return configposy, configposx, configheight, configwidth

def main_window():
    app = tk.Tk()
    app.geometry("800x600")

    def show_frame(frame_name):
        if frame_name == "home":
            home.tkraise()
        elif frame_name == "schedule":
            schedule.tkraise()

    home = gui.home_gui.create_home_frame(app, show_frame)
    schedule = gui.schedule_gui.create_schedule_frame(app, show_frame)

    home.tkraise()
        
    app.mainloop()

if __name__ == "__main__":
    main_window()
