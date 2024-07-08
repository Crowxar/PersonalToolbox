import tkinter as tk


configposy, configposx, configheight, configwidth = app_config()
app = tk.Tk()
app.minsize(configwidth, configheight)
app.geometry(f"{configwidth}x{configheight}+{configposx}+{configposy}")

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