import crowdebug as cdb
import tkinter as tk

root = tk.Tk()
root.geometry("300x500")

root.title("Tkinter Hub")


def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text="☰")
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg="#158aff")

    home_btn = tk.Button(
        toggle_menu_fm,
        text="Home",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    home_btn.place(x=20, y=20)

    products_btn = tk.Button(
        toggle_menu_fm,
        text="Products",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    products_btn.place(x=20, y=80)

    menu_btn = tk.Button(
        toggle_menu_fm,
        text="Menu",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    menu_btn.place(x=20, y=140)

    contacts_btn = tk.Button(
        toggle_menu_fm,
        text="Contacts",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    contacts_btn.place(x=20, y=200)

    feedback_btn = tk.Button(
        toggle_menu_fm,
        text="Feedback",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    feedback_btn.place(x=20, y=260)

    about_btn = tk.Button(
        toggle_menu_fm,
        text="About",
        font=("Bold", 20),
        bd=0,
        bg="#158aff",
        fg="white",
        activebackground="#158aff",
        activeforeground="white",
    )

    about_btn.place(x=20, y=320)

    window_height = root.winfo_height()
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    toggle_btn.config(text="X")
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(
    root, bg="#158aff", highlightbackground="white", highlightthickness=1
)

toggle_btn = tk.Button(
    head_frame,
    text="☰",
    bg="#158aff",
    fg="white",
    font=("Bold", 20),
    bd=0,
    activebackground="#158aff",
    activeforeground="white",
    command=toggle_menu,
)

toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(
    head_frame, text="Tkinter Hub", bg="#158aff", fg="white", font=("Bold", 20)
)

title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


root.mainloop()

cdb.clear_terminal()
