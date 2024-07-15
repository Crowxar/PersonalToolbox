import tkinter as tk
from frames import HomeFrame, SettingsFrame

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(fill='both', expand=True)

        # Create the top bar frame
        top_bar = tk.Frame(self.container, bg="#543D2B", height=30)
        top_bar.pack(side=tk.TOP, fill='x')

        # Create the toggle button
        toggle_button = tk.Button(top_bar, text="☰", bg='red', fg='green', font=("Bold", 20), bd=0,
                                activebackground='pink',
                                activeforeground='blue',
                                command=lambda: print("Test")
                                )
        toggle_button.pack(side=tk.LEFT, fill='y', anchor='w', expand=False)

        self.frames = {}
        for F in (HomeFrame, SettingsFrame):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.pack(fill="both", expand=True)

        self.show_frame("HomeFrame")

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames[page_name]
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.title("Home")
    app.geometry("960x540+480+270")
    app.mainloop()

