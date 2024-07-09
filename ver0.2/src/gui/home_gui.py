import tkinter as tk

def create_home_frame(app, show_frame):
    home = tk.Frame(app, bg="#FFAB7C", bd=0)
    home.pack(fill="both", expand=True)

    menu_bar = tk.Frame(home, bg="#A03900", height=80)
    menu_bar.pack(expand=False, fill="x", side=tk.TOP)

    return home
