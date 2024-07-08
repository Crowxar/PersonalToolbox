import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create a tkinter window
root = tk.Tk()
root.title("Uniform Button Size Example")

# Create a ttkbootstrap style
style = Style(theme='flatly')

# Set a consistent size for all buttons
style.configure('TButton', width=15, padding=10)

# Create some buttons
button1 = ttk.Button(root, text="Button 1 THIS IS A TEST")
button2 = ttk.Button(root, text="Button 2")
button3 = ttk.Button(root, text="Button 3")

# Pack the buttons into the window
button1.pack(pady=10, ipady=40)
button2.pack(pady=10, ipady=40)
button3.pack(pady=10, ipady=40)

# Run the tkinter main loop
root.mainloop()
