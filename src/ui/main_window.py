import tkinter as tk

from .tree_panel import TreePanel
from .canvas_area import CanvasArea
from .property_editor import PropertyEditor

DEFAULT_TREE_WIDTH= 220
COLLAPSED_TREE_WIDTH = 35

class MainWindow(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Tkinter UI Creator")
        self.geometry("1200x800")

        self.collapsed = False
        self._setup_layout()
        self._setup_binds()

    def _setup_layout(self):
        self.canvas = CanvasArea(self)
        self.tree_panel = TreePanel(self)
        self.property_editor = PropertyEditor(self)

        self.canvas.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.tree_panel.place(x=0, y=0, width=DEFAULT_TREE_WIDTH, relheight=1.0, anchor="nw")
        self.property_editor.place(relx=1.0, y=0, width=300, relheight=1.0, anchor="ne")

    def _setup_binds(self):
        self.tree_panel.button_collapse.configure(command=self._collapse_tree_panel)

    def _collapse_tree_panel(self):
        new_tree_width = COLLAPSED_TREE_WIDTH if not self.collapsed else DEFAULT_TREE_WIDTH
        self.tree_panel.place(x=0, y=0, width=new_tree_width, relheight=1.0)
        self.tree_panel.button_collapse.configure(text='+' if not self.collapsed else '-')

        self.collapsed = not self.collapsed
