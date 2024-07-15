import crowdebug as cdb
import tkinter as tk
import os

def get_file_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "assets_tut", file_name)

# Color Configs
menu_color = "#543D2B"
background_color = '#A08A5E'
text_color = 'white'
button_fg_color = text_color
button_bg_color = menu_color
active_bg_menu = menu_color
active_fg_menu = text_color
debug_1 = 'red'
debug_2 = 'orange'

root = tk.Tk()
root.geometry(cdb.centered_screen())
root.title("Tkinter Combo")

top_bar = tk.Frame(root, bg=menu_color)
top_bar.pack(side=tk.TOP, fill='x')
top_bar.pack_propagate(flag=False)
top_bar.config(height=45)

contents_frame = tk.Frame(root, bg=background_color)
contents_frame.pack(side=tk.TOP, fill='both', expand=True)

toggle_icon = tk.PhotoImage(file=get_file_path("toggle_btn_icon.png"))
home_icon = tk.PhotoImage(file=get_file_path("home_icon.png"))
service_icon = tk.PhotoImage(file=get_file_path("services_icon.png"))
updates_icon = tk.PhotoImage(file=get_file_path("updates_icon.png"))
contact_icon = tk.PhotoImage(file=get_file_path("contact_icon.png"))
about_icon = tk.PhotoImage(file=get_file_path("about_icon.png"))
close_btn_icon = tk.PhotoImage(file=get_file_path("close_btn_icon.png"))

def home_page():
    home_page_fm = tk.Frame(contents_frame)

    lb = tk.Label(home_page_fm, text="Home Page", font=("Bold", 20))
    lb.place(x=100, y=200)

    home_page_fm.pack(fill=tk.BOTH, expand=True)



def toggle_menu():
    # Create the frame if it doesn't exist
    if not hasattr(toggle_menu, 'toggle_menu_frame'):
        toggle_menu.toggle_menu_frame = tk.Frame(contents_frame, bg=menu_color)
        toggle_menu.toggle_menu_frame.pack(side=tk.LEFT, fill='y', anchor='w', expand=False)
        
        initialize_menu_widgets(toggle_menu.toggle_menu_frame)

    toggle_menu_frame = toggle_menu.toggle_menu_frame
    toggle_menu_frame.pack_propagate(flag=False)


    def expand_toggle_menu():
        max_width = max(child.winfo_reqwidth() for child in toggle_menu_frame.winfo_children())
        current_width = toggle_menu_frame.winfo_width()
        if current_width < max_width:
            current_width += 10
            toggle_menu_frame.config(width=current_width)
            root.after(ms=6, func=expand_toggle_menu)

    def collapse_toggle_menu():
        current_width = toggle_menu_frame.winfo_width()
        if current_width > 5:
            current_width -= 10
            toggle_menu_frame.config(width=current_width)
            root.after(ms=6, func=collapse_toggle_menu)
        else:
            toggle_menu_frame.pack_forget()
            toggle_menu_button.config(text="☰")
            toggle_menu_button.config(command=toggle_menu)
            return

    if toggle_menu_button.cget('text') == "☰":
        toggle_menu_frame.pack(side=tk.LEFT, fill='y', anchor='w', expand=False)
        toggle_menu_frame.update()
        expand_toggle_menu()
        toggle_menu_button.config(text="X")
        toggle_menu_button.config(command=collapse_toggle_menu)
    else:
        collapse_toggle_menu()

def initialize_menu_widgets(frame):
    menu = toggle_menu.toggle_menu_frame
    # Package One
    package_one = tk.Frame(menu, bg=button_bg_color)
    home_img = tk.Label(package_one, image=home_icon,
                        bg=button_bg_color,
                        fg=button_fg_color)
    home_label = tk.Label(package_one, text='Home',
                          font=('Bold',24),
                          bg=button_bg_color,
                          fg=button_fg_color)
    package_one.pack(side=tk.TOP, pady=5, fill='x', expand=False, anchor='n')
    home_img.pack(side=tk.LEFT, padx=(5,0), fill='y', expand=False)
    home_label.pack(side=tk.LEFT, padx=(0,5), fill='both', expand=True)
    home_img.bind("<Button-1>", lambda event: frame_clicked('Home'))
    home_label.bind("<Button-1>", lambda event: frame_clicked('Home'))
    # Package Two
    package_two = tk.Frame(menu, bg=button_bg_color)
    schedule_img = tk.Label(package_two, image=service_icon,
                        bg=button_bg_color,
                        fg=button_fg_color)
    schedule_label = tk.Label(package_two, text='Schedule',
                          font=('Bold',24),
                          bg=button_bg_color,
                          fg=button_fg_color)
    package_two.pack(side=tk.TOP, pady=5, fill='x', expand=False, anchor='n')
    schedule_img.pack(side=tk.LEFT, padx=(5,0), fill='y', expand=False)
    schedule_label.pack(side=tk.LEFT, padx=(0,5), fill='both', expand=True)
    schedule_img.bind("<Button-1>", lambda event: frame_clicked('Schedule'))
    schedule_label.bind("<Button-1>", lambda event: frame_clicked('Schedule'))

    # Package Three
    package_three = tk.Frame(menu, bg=button_bg_color)
    package_three.pack(side=tk.TOP, pady=5, fill='x', expand=False, anchor='n')

    about_img = tk.Label(package_three, image=about_icon,
                        bg=button_bg_color,
                        fg=button_fg_color)
    about_label = tk.Label(package_three, text='About',
                          font=('Bold',24),
                          bg=button_bg_color,
                          fg=button_fg_color)
    about_img.pack(side=tk.LEFT, padx=(5,0), fill='y', expand=False)
    about_label.pack(side=tk.LEFT, padx=(0,5), fill='both', expand=True, anchor='e')
    about_img.bind("<Button-1>", lambda event: frame_clicked('About'))
    about_label.bind("<Button-1>", lambda event: frame_clicked('About'))


def frame_clicked(frame):
    print(f"{frame} clicked!")

toggle_menu_button = tk.Button(
    top_bar,
    text="☰",
    bg=button_bg_color,
    fg=button_fg_color,
    font=("Bold", 20),
    bd=0,
    activebackground=active_bg_menu,
    activeforeground=active_fg_menu,
    command=toggle_menu,
)

toggle_menu_button.pack(side=tk.LEFT)


def switch_indication(page):
    menu = toggle_menu.toggle_menu_frame
    if menu.winfo_width() > 45:
        toggle_menu.collapse_toggle_menu()

    for frame in contents_frame.winfo_children():
        frame.destroy()

    page()

root.lift()
root.attributes("-topmost", True)
root.mainloop()
#cdb.clear_terminal()





