import crowdebug as cdb
import tkinter as tk
import os


def get_file_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "assets_tut", file_name)

# Color Configs
button_color = ...
menu_color = "#543D2B"
background_color = '#A08A5E'
text_color = 'white'
active_bg_menu = menu_color
active_fg_menu = text_color
debug_1 = 'red'
debug_2 = 'orange'


root = tk.Tk()
root.geometry(cdb.centered_screen())  # Fix Centered Screen from Debug Import
root.title("Personal Toolbox")

#region Menu Bar Animation

def extend_menu_bar():
    menu_bar_frame.pack(side=tk.LEFT, fill='y')
    toggle_menu_button.config(state=tk.DISABLED)
    extending_animation()

def extending_animation():
    current_width = menu_bar_frame.winfo_width()
    if not current_width > 130:
        current_width += 10
        menu_bar_frame.config(width=current_width)
        root.after(ms=8, func=extending_animation)
        toggle_menu_button.config(text='X', command=fold_menu, state=tk.NORMAL)

def fold_menu():
    toggle_menu_button.config(text='☰', command=extend_menu_bar, state=tk.NORMAL)
    menu_bar_frame.pack_forget()
    

#endregion

#region Title Bar
title_bar = tk.Frame(root, bg=menu_color)
total_contents_frame = tk.Frame(root, bg=background_color)
title_bar.pack(side=tk.TOP, fill=tk.X)
total_contents_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
title_bar.pack_propagate(flag=False)
title_bar.config(height=45)

toggle_menu_button = tk.Button(title_bar, text='☰',
    font=("Bold", 20),
    bd=0, bg=menu_color,
    fg=text_color,
    activebackground=active_bg_menu,
    activeforeground=active_fg_menu,
    command=extend_menu_bar
)
toggle_menu_button.pack(side=tk.LEFT)

menu_bar_frame = tk.Frame(total_contents_frame, bg=menu_color)
menu_bar_frame.pack(side=tk.LEFT, fill='y', expand=True)
menu_bar_frame.pack_forget()

active_content = tk.Frame(total_contents_frame, bg=background_color)
active_content.pack(side=tk.RIGHT, fill='both', expand=True)



title_label = tk.Label(title_bar, text="Home",
    font=("Bold", 20),
    bg=menu_color,
    fg=text_color
    )
title_label.pack(side=tk.LEFT, padx=0, fill='both')

#endregion

menu_pane_one = tk.Frame(menu_bar_frame,bg=debug_1)
menu_pane_one.pack(side=tk.TOP, pady=(5,0), fill='x', expand=True, anchor='n')
label_one = tk.Label(menu_pane_one,text='Test Label', font=('Bold',20))
label_one_img = tk.Label(menu_pane_one,text='☰', font=('Bold',20))
label_one_img.pack(side='left')
label_one.pack(side='right', fill='both')





# pin to top and start app, clear terminal afterwards
root.lift()
root.attributes("-topmost", True)
root.mainloop()
cdb.clear_terminal()
