import crowdebug as cdb
import tkinter as tk
import os


def get_file_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "assets_tut", file_name)


# region DebugColors
debug_button_colors = 0

if debug_button_colors == 1:
    menubar_color = "#D38C8C"
    button_bg_color = "#D3CB8C"
else:
    menubar_color = "#383838"
    button_bg_color = "#383838"

# endregion


root = tk.Tk()
root.geometry(cdb.centered_screen())
root.title("Tkinter Hub Project 2")

# Icons
toggle_icon = tk.PhotoImage(file=get_file_path("toggle_btn_icon.png"))
home_icon = tk.PhotoImage(file=get_file_path("home_icon.png"))
service_icon = tk.PhotoImage(file=get_file_path("services_icon.png"))
updates_icon = tk.PhotoImage(file=get_file_path("updates_icon.png"))
contact_icon = tk.PhotoImage(file=get_file_path("contact_icon.png"))
about_icon = tk.PhotoImage(file=get_file_path("about_icon.png"))
close_btn_icon = tk.PhotoImage(file=get_file_path("close_btn_icon.png"))


def switch_indication(indicator_lb, page):
    home_btn_ind.config(bg=menubar_color)
    service_btn_ind.config(bg=menubar_color)
    updates_btn_ind.config(bg=menubar_color)
    contact_btn_ind.config(bg=menubar_color)
    about_btn_ind.config(bg=menubar_color)
    indicator_lb.config(bg="white")

    if menu_bar_frame.winfo_width() > 45:
        fold_menu()

    for frame in page_frame.winfo_children():
        frame.destroy()

    page()


def extending_animation():
    current_width = menu_bar_frame.winfo_width()
    if not current_width > 130:
        current_width += 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=8, func=extending_animation)


def fold_animation():
    current_width = menu_bar_frame.winfo_width()
    if current_width != 45:
        current_width -= 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=8, func=fold_animation)


def extend_menu_bar():
    extending_animation()
    toggle_menu_btn.config(image=close_btn_icon)
    toggle_menu_btn.config(command=fold_menu)


def fold_menu():
    fold_animation()
    toggle_menu_btn.config(image=toggle_icon)
    toggle_menu_btn.config(command=extend_menu_bar)


def home_page():
    home_page_fm = tk.Frame(page_frame)

    lb = tk.Label(home_page_fm, text="Home Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    home_page_fm.pack(fill=tk.BOTH, expand=True)


def service_page():
    service_page_fm = tk.Frame(page_frame)

    lb = tk.Label(service_page_fm, text="Service Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    service_page_fm.pack(fill=tk.BOTH, expand=True)


def update_page():
    update_page_fm = tk.Frame(page_frame)

    lb = tk.Label(update_page_fm, text="Update Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    update_page_fm.pack(fill=tk.BOTH, expand=True)


def contact_page():
    contact_page_fm = tk.Frame(page_frame)

    lb = tk.Label(contact_page_fm, text="Contact Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    contact_page_fm.pack(fill=tk.BOTH, expand=True)


def about_page():
    about_page_fm = tk.Frame(page_frame)

    lb = tk.Label(about_page_fm, text="About Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    about_page_fm.pack(fill=tk.BOTH, expand=True)


page_frame = tk.Frame(root)
page_frame.place(relwidth=1.0, relheight=1.0, x=50)
home_page()


menu_bar_frame = tk.Frame(root, bg=menubar_color)
menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate(flag=False)
menu_bar_frame.configure(width=45)


# Buttons
toggle_menu_btn = tk.Button(
    menu_bar_frame,
    image=toggle_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=extend_menu_bar,
)
toggle_menu_btn.place(x=4, y=10)


# individual frames
home_btn = tk.Button(
    menu_bar_frame,
    image=home_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=lambda: switch_indication(home_btn_ind, home_page),
)
home_btn.place(x=9, y=130, width=30, height=40)
home_btn_ind = tk.Label(menu_bar_frame, bg="white")
home_btn_ind.place(x=3, y=130, width=3, height=40)

home_page_lb = tk.Label(
    menu_bar_frame,
    text="Home",
    bg=menubar_color,
    fg="white",
    font=("Bold", 15),
    anchor=tk.W,
)
home_page_lb.place(x=45, y=130, width=100, height=40)
home_page_lb.bind(
    "<Button-1>", lambda e: switch_indication(indicator_lb=home_btn_ind, page=home_page)
)


service_btn = tk.Button(
    menu_bar_frame,
    image=service_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=lambda: switch_indication(service_btn_ind, service_page),
)
service_btn.place(x=9, y=190, width=30, height=40)
service_btn_ind = tk.Label(menu_bar_frame, bg=menubar_color)
service_btn_ind.place(x=3, y=190, width=3, height=40)

service_page_lb = tk.Label(
    menu_bar_frame,
    text="Service",
    bg=menubar_color,
    fg="white",
    font=("Bold", 15),
    anchor=tk.W,
)
service_page_lb.place(x=45, y=190, width=100, height=40)
service_page_lb.bind(
    "<Button-1>",
    lambda e: switch_indication(indicator_lb=service_btn_ind, page=service_page),
)


updates_btn = tk.Button(
    menu_bar_frame,
    image=updates_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=lambda: switch_indication(updates_btn_ind, update_page),
)
updates_btn.place(x=9, y=250, width=30, height=40)
updates_btn_ind = tk.Label(menu_bar_frame, bg=menubar_color)
updates_btn_ind.place(x=3, y=250, width=3, height=40)
updates_page_lb = tk.Label(
    menu_bar_frame,
    text="Updates",
    bg=menubar_color,
    fg="white",
    font=("Bold", 15),
    anchor=tk.W,
)
updates_page_lb.place(x=45, y=250, width=100, height=40)
updates_page_lb.bind(
    "<Button-1>",
    lambda e: switch_indication(indicator_lb=updates_btn_ind, page=update_page),
)


contact_btn = tk.Button(
    menu_bar_frame,
    image=contact_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=lambda: switch_indication(contact_btn_ind, contact_page),
)
contact_btn.place(x=9, y=310, width=30, height=40)
contact_btn_ind = tk.Label(menu_bar_frame, bg=menubar_color)
contact_btn_ind.place(x=3, y=310, width=3, height=40)

contact_page_lb = tk.Label(
    menu_bar_frame,
    text="Contact",
    bg=menubar_color,
    fg="white",
    font=("Bold", 15),
    anchor=tk.W,
)
contact_page_lb.place(x=45, y=310, width=100, height=40)
contact_page_lb.bind(
    "<Button-1>",
    lambda e: switch_indication(indicator_lb=contact_btn_ind, page=contact_page),
)


about_btn = tk.Button(
    menu_bar_frame,
    image=about_icon,
    bg=button_bg_color,
    bd=0,
    activebackground=button_bg_color,
    activeforeground="white",
    command=lambda: switch_indication(about_btn_ind, about_page),
)
about_btn.place(x=9, y=370, width=30, height=40)
about_btn_ind = tk.Label(menu_bar_frame, bg=menubar_color)
about_btn_ind.place(x=3, y=370, width=3, height=40)

about_page_lb = tk.Label(
    menu_bar_frame,
    text="About",
    bg=menubar_color,
    fg="white",
    font=("Bold", 15),
    anchor=tk.W,
)
about_page_lb.place(x=45, y=370, width=100, height=40)
about_page_lb.bind(
    "<Button-1>",
    lambda e: switch_indication(indicator_lb=about_btn_ind, page=about_page),
)


root.lift()
root.attributes("-topmost", True)

root.mainloop()
cdb.clear_terminal()



