from ttkbootstrap.constants import *  # noqa: F403
import configparser as cp
import crowdebug as cdb
import tkinter as tk
import utils as u
import markdown2
import os as os


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
def show_frame(frame):
    # Hide all frames
    for f in (home, schedule):
        f.pack_forget()
    # Show the selected frame
    frame.pack(fill="both", expand=True)


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
    command=lambda: display_license(),
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
def display_license():
    license_window = tk.Toplevel()
    license_window.title("License Information")


    current_dir = os.path.dirname(__file__)  # Get the current directory of the script
    license_path = os.path.abspath(os.path.join(current_dir, '..', 'license.md'))
    with open(license_path, 'r', encoding='utf-8') as file:
        license_text = file.read()


    license_to_HTML = markdown2.markdown(license_text)

    text_widget = tk.scrolledtext.ScrolledText(license_window, wrap=tk.WORD, width=80, height=20)
    text_widget.insert(tk.END, license_to_HTML)
    text_widget.configure(state='disabled')
    text_widget.pack(expand=True, fill=tk.BOTH)

    


# endregion




show_frame(home)
app.mainloop()
