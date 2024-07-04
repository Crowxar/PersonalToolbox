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

# Base Layout
schedule = ttk.Frame(app, style='DBGRED.TFrame')
menu_bar = ttk.Frame(schedule, style='DBGYEL.TFrame', height=50)
homebtn_frame = ttk.Frame(menu_bar, style='DBGGRE.TFrame', height=50, width=80)
homebutton = ttk.Button(homebtn_frame, text="Home", command=lambda: show_frame(home), bootstyle=WARNING, takefocus=False)
exitbtn_frame = ttk.Frame(menu_bar, style='DBGGRE.TFrame', height=50, width=80)
exitbutton = ttk.Button(exitbtn_frame, text="Exit", command=lambda: exit_func(), bootstyle=WARNING, takefocus=False)
schedule_title = ttk.Label(menu_bar, text='Schedule Page',bootstyle="info", font='times 24')
main_contents = ttk.Frame(schedule, style='DBGORA.TFrame')

schedule.pack(fill='both', expand=True)
menu_bar.pack(side=tk.TOP, fill='x',expand=False)
homebtn_frame.pack(expand=False, side=tk.LEFT)
homebutton.pack() #command=lambda: show_frame(home) command=lambda: DBG.button_test("Home")
exitbtn_frame.pack(expand=False, side=tk.RIGHT)
exitbutton.pack()
schedule_title.pack()
main_contents.pack(side=tk.TOP,fill="both", expand=True, padx=10, pady=10)

# Content Containers
pilots_section = ttk.Frame(main_contents, style='DBGYEL.TFrame')
output_section = ttk.Frame(main_contents, style='DBGYEL.TFrame', width=400)
input_section = ttk.Frame(main_contents, style='DBGYEL.TFrame')

pilots_section.pack(side=tk.LEFT, fill='both',expand=False, padx=(10,5), pady=10)
output_section.pack(side=tk.LEFT, fill='both',expand=True, padx=(5,5), pady=10)
input_section.pack(side=tk.LEFT, fill='both', expand=False, padx=(5,10), pady=10)

# Pilot Container Contents
pilot_frames = []
for pilot_name in pilot_list:
    pilot_frame = ttk.Frame(pilots_section, style='DBGGRE.TFrame', height=30)
    pilot_frame.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=2)
    pilot_frames.append(pilot_frame)

for i, pilot_frame in enumerate(pilot_frames):
    label_text = f"{pilot_list[i]}"
    label = ttk.Label(pilot_frame, text=label_text, style="danger.TLabel", font='times 15')
    label.pack(side=tk.LEFT, fill='both')
    select_button = ttk.Checkbutton(pilot_frame, bootstyle ="round-toggle", command=lambda text=label_text: DBG.button_toggle_test(text))
    select_button.pack(side=tk.RIGHT, fill='y', padx=(5,0))

# Input Container Contents
entry_container = ttk.Frame(input_section, style='DBGGRE.TFrame', height=200)
buttons_container = ttk.Frame(input_section, style='DBGGRE.TFrame', height=200)

entry_container.pack(side=tk.TOP, fill='both', expand=True, padx=10, pady=10, anchor=tk.N)
buttons_container.pack(side=tk.TOP, fill='both', expand=True, padx=10, pady=10, anchor=tk.N)

textbox_section = ttk.Frame(entry_container, style='DBGBLU.TFrame', height=5)
textbox_section.pack(fill="both", expand=True, padx=5,pady=5)

brieflable = ttk.Labelframe(textbox_section, bootstyle="info", text="Brief Time")
brieftime = ttk.Entry(brieflable, bootstyle="danger")
brieflable.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=5, anchor=N)
brieftime.pack(side=tk.TOP, fill='x', expand=True, padx=5,pady=5, anchor=N)

takeofflable = ttk.Labelframe(textbox_section, bootstyle="info", text="Take Off Time")
takeofftime = ttk.Entry(takeofflable, bootstyle="danger")
takeofflable.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=5, anchor=N)
takeofftime.pack(side=tk.TOP, fill='x', expand=True, padx=5,pady=5, anchor=N)

landinglable = ttk.Labelframe(textbox_section, bootstyle="info", text="Landing Time")
landingtime = ttk.Entry(landinglable, bootstyle="danger")
landinglable.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=5, anchor=N)
landingtime.pack(side=tk.TOP, fill='x', expand=True, padx=5,pady=5, anchor=N)


#Buttons Container Contents
button1 = ttk.Button(buttons_container, text="Submit", command=lambda: DBG.button_toggle_test("Submit"), bootstyle=WARNING, takefocus=False)
button2 = ttk.Button(buttons_container, text="Clear", command=lambda: DBG.button_toggle_test("Clear"), bootstyle=WARNING, takefocus=False)
button3 = ttk.Button(buttons_container, text="Complete", command=lambda: DBG.button_toggle_test("Complete"), bootstyle=WARNING, takefocus=False)

button1.pack(side=tk.LEFT, fill="both", expand=True, padx=5,pady=5)
button2.pack(side=tk.LEFT, fill="both", expand=True, padx=5,pady=5)
button3.pack(side=tk.LEFT, fill="both", expand=True, padx=5,pady=5)

#Output Container Contents
outputlabel = ttk.Labelframe(output_section, bootstyle="info", text="Output")
outputtext = tk.Text(outputlabel, width=50)
outputlabel.pack(side=tk.TOP, fill='both', expand=True, padx=5, pady=5, anchor=N)
outputtext.pack(side=tk.TOP, fill='both', expand=True, padx=5,pady=5, anchor=N)

#Second Button Container
pilotbuttons = ttk.Frame(output_section, style='DBGGRE.TFrame', height=200)
pilotbuttons.pack(fill='both', expand=True, padx=5, pady=5)

button1 = ttk.Button(pilotbuttons, text="Add Pilot", command=lambda: DBG.button_toggle_test("Add Pilot"), bootstyle=WARNING, takefocus=False)
button2 = ttk.Button(pilotbuttons, text="Remove Pilot", command=lambda: DBG.button_toggle_test("Remove Pilot"), bootstyle=WARNING, takefocus=False)

button1.pack(side=tk.LEFT, fill="both", expand=True, padx=5,pady=5)
button2.pack(side=tk.LEFT, fill="both", expand=True, padx=5,pady=5)

"""

#(side, fill, expand, padx, pady, ipadx, ipady, anchor, before, after)

"""





# endregion

show_frame(schedule)

app.mainloop()
DBG.clear_terminal()