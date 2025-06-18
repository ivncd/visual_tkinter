import tkinter as tk
from tkinter import ttk

from ui.main_window import MainWindow 


def load_editor_theme():
    style = ttk.Style()
    style.configure("Editor.TFrame", background="#ababab")
    style.configure("Canvas.TFrame", background="#ffffff", highlightbackground="#cccccc", highlightthickness=1)
    style.configure("Tree.TFrame", background="#e6e6e6")
    style.configure("Root.TFrame", background="#f0f0f5")


window = MainWindow()
load_editor_theme()
window.mainloop()
