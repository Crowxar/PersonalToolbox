import tkinter as tk
import configparser as cp
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import lamdebug as DBG


pilot_list = ["Botzer", "Hempen", "Landry", "O'Neil", "Turner", "Griffin", "Segreti"]

# region ================== Screen Size Configuration ==================
config_file = 'config.ini'
config = cp.ConfigParser()

def get_screen_size():
    sizeroot = tk.Tk()
    screen_width, screen_height = sizeroot.winfo_screenwidth(), sizeroot.winfo_screenheight()
    config['Screen Size'] = {'width': screen_width, 'height': screen_height}
    sizeroot.destroy()
    default_width, default_height = screen_width // 2, screen_height // 2
    config['Default Window Size'] = {'width': default_width, 'height': default_height}
    default_x, default_y = default_width // 2, default_height // 2 
    config['Default Position'] = {'x': default_x, 'y': default_y}
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def default_config_check():
    checks = [
        ('Screen Size', 'width'),
        ('Screen Size', 'height'),
        ('Default Window Size', 'width'),
        ('Default Window Size', 'height'),
        ('Default Position', 'x'),
        ('Default Position', 'y')
    ]

    for section, option in checks:
        if not config.has_option(section, option):
            get_screen_size()
            break

# endregion

# region ================== App Configuration ==================
def show_frame(frame):
    # Hide all frames
    for f in (home, schedule):
        f.pack_forget()
    # Show the selected frame
    frame.pack(fill='both', expand=True)

app = tk.Tk()

config.read('config.ini')
configwidth = config.getint('Default Window Size', 'width')
configheight = config.getint('Default Window Size', 'height')
configposx = config.getint('Default Position', 'x')
configposy = config.getint('Default Position', 'y')
app.minsize(configwidth, configheight)
app.geometry(f"{configwidth}x{configheight}+{configposx}+{configposy}")
style = ttk.Style(theme='superhero')
#style.configure('TCheckbutton', font = 22)

# endregion

# region ================== Home Screen Code ==================
home = tk.Frame(app)
home.pack(fill='both', expand=True)

header_label = tk.Label(home, text="Application Title", font=("Arial", 18))
subheader_label = tk.Label(home, text="Select Options Below", font=("Arial", 14))
header_label.pack(pady=20)
subheader_label.pack(pady=20)

def Button_A_Toggle():
    otherbutton1.configure(state=tk.DISABLED)
    otherbutton2.configure(state=tk.ACTIVE)

def Button_B_Toggle():
    otherbutton2.configure(state=tk.DISABLED)
    otherbutton1.configure(state=tk.ACTIVE)

def exit_func():
    print("Program Exited")
    app.destroy()

def schedule_func():
    print("Schedule_page")

def Test_button_func():
    print("Test Button Pressed")

bottom_button_frame = tk.Frame(home)
bottom_button_frame.pack(side=tk.BOTTOM, pady=20)
style.configure('TButton', width=15, padding=10)


schedulebutton = ttk.Button(bottom_button_frame, text="Schedule", command=lambda: show_frame(schedule), bootstyle=WARNING, takefocus=False)
otherbutton1 = ttk.Button(bottom_button_frame, text="Toggle A", command=Button_A_Toggle, bootstyle=WARNING, state=DISABLED, takefocus=False)
otherbutton2 = ttk.Button(bottom_button_frame, text="Toggle B", command=Button_B_Toggle, bootstyle=WARNING, state=ACTIVE, takefocus=False)
otherbutton3 = ttk.Button(bottom_button_frame, text="Test", command=Test_button_func, bootstyle=WARNING, takefocus=False)
exitbutton = ttk.Button(bottom_button_frame, text="Exit", command=exit_func, bootstyle=WARNING, takefocus=False)

button_spacing, button_height = 5, 30
schedulebutton.pack(side=tk.LEFT, padx=button_spacing, ipady=button_height)
otherbutton1.pack(side=tk.LEFT, padx=button_spacing, ipady=button_height)
otherbutton2.pack(side=tk.LEFT, padx=button_spacing, ipady=button_height)
otherbutton3.pack(side=tk.LEFT, padx=button_spacing, ipady=button_height)
exitbutton.pack(side=tk.LEFT, padx=button_spacing, ipady=button_height)
# endregion

# region ================== Schedule Frame Code ==================
#DBG.setup_styles()
# region ================== Schedule Screen Code =======================
schedule = tk.Frame(app, bg="#FFAB7C", bd=0)
schedule.pack(fill='both', expand=True)

menu_bar_sch = tk.Frame(home, bg="#A03900", height=80)
menu_bar_sch.pack(expand=False, fill='x', side=TOP)

home_image = tk.PhotoImage(file=u.asset_path("home_frame", "home.png"))
homebutton_sch = tk.Button(menu_bar_sch, image=home_image,
                        borderwidth=0, highlightthickness=0, relief="flat",
                        command=lambda: print("Home clicked")
                        )
homebutton_sch.pack(side=tk.LEFT)

# endregion

show_frame(schedule)

app.mainloop()
DBG.clear_terminal()