import tkinter as tk
from tkinter import ttk
import sv_ttk

from .tree_panel import TreePanel
from .design_area import DesignArea
from .property_editor import PropertyEditor

DEFAULT_TREE_WIDTH= 220
COLLAPSED_TREE_WIDTH = 10
BUTTON_PADDING = 12

def load_editor_theme():
    style = ttk.Style()
    #style.configure("Treeview", background="black", fieldbackground="black", foreground="white")
    style.configure("Editor.TFrame", background="#ababab")
    style.configure("Canvas.TFrame", background="#aaaaaa")
    style.configure("Tree.TFrame", background="#e6e6e6")
    style.configure("Root.TFrame", background="#f0f0f5")

class MainWindow(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Tkinter UI Creator")
        self.geometry("1200x800")

        load_editor_theme()
        #sv_ttk.set_theme("light")
        self.collapsed = False
        self._setup_layout()

    def _setup_layout(self):
        self.design_area = DesignArea(self)
        self.tree_panel = TreePanel(self)
        self.button_collapse = ttk.Button(self, text="<")
        #self.property_editor = PropertyEditor(self)

        self.design_area.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.tree_panel.place(x=0, y=0, width=DEFAULT_TREE_WIDTH, relheight=1.0, anchor="nw")
        self.button_collapse.place(x=DEFAULT_TREE_WIDTH + BUTTON_PADDING, rely=0.5, height=50, width=20, anchor="e")
        #self.property_editor.place(relx=1.0, y=0, width=300, relheight=1.0, anchor="ne")
