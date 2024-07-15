import tkinter as tk
from frames import HomeFrame, SettingsFrame

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

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
    app.geometry("400x300")
    app.mainloop()
