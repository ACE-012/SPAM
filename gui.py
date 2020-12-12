import tkinter as tk
import threading
class GUI(threading.Thread):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.colourselection= ['red', 'green','grey']
        self.colourselectionno=0
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), borderwidth=0, highlightthickness=0, bg="white")
    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle = _create_circle
    def create(self):
        self.canvas.grid()
        self.canvas.create_circle((self.root.winfo_screenwidth()-100), 120, 50, fill=self.colourselection[self.colourselectionno], outline="#DDD", width=4)
        self.root.mainloop()
    def exit(self):
        self.root.quit()
    def changecol(self):
        self.canvas.create_circle((self.root.winfo_screenwidth()-100), 120, 50, fill=self.colourselection[self.colourselectionno], outline="#DDD", width=4)