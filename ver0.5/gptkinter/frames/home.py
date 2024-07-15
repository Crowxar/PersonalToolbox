import tkinter as tk
from tkinter import ttk
from button_functions import go_to_settings

class HomeFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        
        label = ttk.Label(self, text="Home Frame", font=("Arial", 24))
        label.pack(pady=10)

        button = ttk.Button(self, text="Go to Settings", command=lambda: go_to_settings(self.controller))
        button.pack(pady=20)

