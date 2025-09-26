import tkinter as tk
from tkinter import ttk

class DesignArea(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(style="Canvas.TFrame")


