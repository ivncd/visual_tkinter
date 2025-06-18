import tkinter as tk
from tkinter import ttk

class TreePanel(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(style="Tree.TFrame")

        self._setup_layout()
        self._setup_widgets()

    def _setup_widgets(self):
        self.button_collapse = ttk.Button(self, text="-", width=3)
        self.button_collapse.grid(row=0, rowspan=2, column=1, sticky="ne", padx=3)

    def _setup_layout(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
