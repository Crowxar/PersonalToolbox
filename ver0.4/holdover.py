# region Package One
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
#endregion
# region Package Two
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
#endregion
# region Package Three
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
#endregion