import tkinter as tk
from tkinter import ttk

from .editable_treeview import EditableTreeview

class TreeFrame(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)

        self._setup_layout()
        self._setup_widgets()

    def _setup_widgets(self):
        self.tree = EditableTreeview(self)
        self.tree.heading("#0", text="WIDGETS")
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 20))

    def _setup_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


