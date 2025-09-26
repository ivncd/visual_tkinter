import tkinter as tk
from tkinter import ttk

CONTAINER = "container"
WIDGET = "widget"
HIGHLIGHT_CONTAIN = "highlight_contain"

class EditableTreeview(ttk.Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.menu = tk.Menu(self, tearoff=0)

        self.tag_configure(HIGHLIGHT_CONTAIN, background="#d0f0ff")
        self._populate_example()


    def _populate_example(self):
        frame_id = self.insert("", "end", text="Frame", tags=(CONTAINER,))
        box_id = self.insert("", "end", text="VBox", tags=(CONTAINER,))
        grid_id = self.insert("", "end", text="Grid", tags=(CONTAINER,))

        self.insert(frame_id, "end", text="Label", tags=("widget",))
        self.insert(frame_id, "end", text="Button", tags=("widget",))
        self.insert(box_id, "end", text="Entry", tags=("widget",))
        self.insert(box_id, "end", text="Checkbutton", tags=("widget",))
        self.insert(grid_id, "end", text="Canvas", tags=("widget",))
        self.insert("", "end", text="Standalone Button", tags=("widget",))

