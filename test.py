from tkinterweb import HtmlFrame #import the HTML browser
import tkinter as tk #python3
import os
import markdown2





current_dir = os.path.dirname(__file__)  # Get the current directory of the script
license_path = os.path.abspath(os.path.join(current_dir, '..', 'LICENSE.md'))

if os.path.exists(license_path):
    print(f"File '{license_path}' exists.")
else:
    print(f"File '{license_path}' does not exist.")




"""license_to_HTML = markdown2.markdown(license_text)


root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create the HTML browser
frame.load_file(LICENSE.md) #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()"""