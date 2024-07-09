import tkinter as tk

def create_schedule_frame(app, show_frame):
    schedule = tk.Frame(app, bg="#FFAB7C", bd=0)
    schedule.pack(fill="both", expand=True)

    menu_bar_sch = tk.Frame(schedule, bg="#A03900", height=80)
    menu_bar_sch.pack(expand=False, fill="x", side=tk.TOP)

    return schedule
