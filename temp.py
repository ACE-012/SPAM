import tkinter as tk
from overlay import Window

win_0 = Window()
label_0 = tk.Label(win_0.root, text="Window_0")
label_0.pack()
win_1 = Window()
label_1 = tk.Label(win_1.root, text="Window_1")
label_1.pack()
Window.launch()