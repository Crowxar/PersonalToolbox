from ttkbootstrap.constants import *  # noqa: F403
import configparser as cp
import crowdebug as cdb
import tkinter as tk
import utils as u
import os as os
from tkinterweb import HtmlFrame


# region ================== Screen Size Configuration ==================
config_file = "config.ini"
config = cp.ConfigParser()


def get_screen_size():
    cdb.log.info("Getting Screen Size")
    sizeroot = tk.Tk()
    screen_width, screen_height = (
        sizeroot.winfo_screenwidth(),
        sizeroot.winfo_screenheight(),
    )
    config["Screen Size"] = {"width": screen_width, "height": screen_height}
    sizeroot.destroy()
    default_width, default_height = screen_width // 2, screen_height // 2
    config["Default Window Size"] = {"width": default_width, "height": default_height}
    default_x, default_y = default_width // 2, default_height // 2
    config["Default Position"] = {"x": default_x, "y": default_y}
    with open(config_file, "w") as configfile:
        cdb.log.info("Writing Config.ini")
        config.write(configfile)


def default_config_check():
    cdb.log.info("Checking config.ini for default settings")
    checks = [
        ("Screen Size", "width"),
        ("Screen Size", "height"),
        ("Default Window Size", "width"),
        ("Default Window Size", "height"),
        ("Default Position", "x"),
        ("Default Position", "y"),
    ]

    for section, option in checks:
        if not config.has_option(section, option):
            cdb.log.warning(f"Config.ini did not have {section}. Attempting to rewrite")
            get_screen_size()
            break


# endregion

# region ================== App Configuration ==========================



def app_config():
    default_config_check()
    config.read("config.ini")
    configwidth = config.getint("Default Window Size", "width")
    configheight = config.getint("Default Window Size", "height")
    configposx = config.getint("Default Position", "x")
    configposy = config.getint("Default Position", "y")
    return configposy, configposx, configheight, configwidth


configposy, configposx, configheight, configwidth = app_config()
app = tk.Tk()
app.minsize(configwidth, configheight)
app.geometry(f"{configwidth}x{configheight}+{configposx}+{configposy}")


# endregion

# region ================== Home Screen Code ===========================

home = tk.Frame(app, bg="#FFAB7C", bd=0)
home.pack(fill="both", expand=True)

menu_bar = tk.Frame(home, bg="#A03900", height=80)
menu_bar.pack(expand=False, fill="x", side=TOP)  # noqa: F405

legal_bar = tk.Frame(home, bg="#ffab7c", height=80)
legal_bar.pack(expand=False, fill="x", side=BOTTOM)  # noqa: F405

license_image = tk.PhotoImage(file=u.asset_path("licenses.png"))
licensebutton = tk.Button(
    legal_bar,
    image=license_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: show_frame(license_frame),
)
licensebutton.pack(side=tk.RIGHT)

info_image = tk.PhotoImage(file=u.asset_path("info.png"))
infobutton = tk.Button(
    legal_bar,
    image=info_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: print("Info clicked"),
)
infobutton.pack(side=tk.RIGHT)

home_image = tk.PhotoImage(file=u.asset_path("home.png"))
homebutton = tk.Button(
    menu_bar,
    image=home_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: print("Home clicked"),
)
homebutton.pack(side=tk.LEFT)

schedule_image = tk.PhotoImage(file=u.asset_path("schedule.png"))
schedulebutton = tk.Button(
    menu_bar,
    image=schedule_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: show_frame(schedule),
)
schedulebutton.pack(side=tk.LEFT)
# endregion

# region ================== Schedule Screen Code =======================
schedule = tk.Frame(app, bg="#FFAB7C", bd=0)

menu_bar_sch = tk.Frame(schedule, bg="#A03900", height=80)
menu_bar_sch.pack(expand=False, fill="x", side=TOP)  # noqa: F405

home_image_sch = tk.PhotoImage(file=u.asset_path("home.png"))
homebutton_sch = tk.Button(
    menu_bar_sch,
    image=home_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: show_frame(home),
)
homebutton_sch.pack(side=tk.LEFT)

# endregion

# region ================== License Window Code ========================
license_frame = tk.Frame(app, bg="#FFAB7C", bd=0)

menu_bar_lic = tk.Frame(license_frame, bg="#A03900", height=80)
menu_bar_lic.pack(expand=False, fill="x", side=TOP)  # noqa: F405

home_image_lic = tk.PhotoImage(file=u.asset_path("home.png"))
homebutton_lic = tk.Button(
    menu_bar_lic,
    image=home_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: show_frame(home),
)
homebutton_lic.pack(side=tk.LEFT)

legal_bar_lic = tk.Frame(license_frame, bg="#ffab7c", height=80)
legal_bar_lic.pack(expand=False, fill="x", side=BOTTOM)  # noqa: F405

license_image_lic = tk.PhotoImage(file=u.asset_path("licenses.png"))
licensebutton_lic = tk.Button(
    legal_bar_lic,
    image=license_image_lic,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: print("License Clicked"),
)
licensebutton_lic.pack(side=tk.RIGHT)

info_image_lic = tk.PhotoImage(file=u.asset_path("info.png"))
infobutton_lic = tk.Button(
    legal_bar_lic,
    image=info_image_lic,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: print("Info clicked"),
)
infobutton_lic.pack(side=tk.RIGHT)

#ADD THIS TO LICENSE INFO TO BE DISPLAYED 
""" 
def display_license():
    license_window = tk.Toplevel()
    license_window.title("License Information")

    license_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LICENSE.md'))
    html_frame = HtmlFrame(license_window)
    html_frame.load_file(u.create_HTML_file(license_path))
    html_frame.pack(fill="both", expand=True)

    license_window.focus_set()  # Set focus to the license window
    license_window.grab_set()
    show_frame(home)
"""

# endregion




show_frame(home)
app.mainloop()
