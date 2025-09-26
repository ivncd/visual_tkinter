import tkinter as tk
from tkinter import ttk

from .widgets_frame import WidgetsFrame
from .tree_frame import TreeFrame

class TreePanel(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(style="Tree.TFrame")

        self._setup_layout()
        self._setup_widgets()

    def _setup_widgets(self):
        self.frame_widgets = WidgetsFrame(self)
        self.frame_widgets.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=10, pady=5)

        self.frame_tree = TreeFrame(self, style="Treeview")
        self.frame_tree.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)


    def _setup_layout(self):
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
