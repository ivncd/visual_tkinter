from core.treeview_manager import TreeviewManager
from ui.design_area import DesignArea
from ui.components import CONTAINER

import tkinter as tk
from tkinter import ttk

CONTAINERS = ["Frame", "LabelFrame", "Canvas"]

WIDGET_CLASSES = {
    # Containers
    "Frame": ttk.Frame,
    "LabelFrame": ttk.LabelFrame,
    "Canvas": tk.Canvas,

    # Basic widgets
    "Button": ttk.Button,
    "Label": ttk.Label,
    "Entry": ttk.Entry,
    "Text": tk.Text,
    "Message": tk.Message,

    # Selection and input
    "Checkbutton": ttk.Checkbutton,
    "Radiobutton": ttk.Radiobutton,
    "Spinbox": tk.Spinbox,
    "Listbox": tk.Listbox,
    "Scale": ttk.Scale,
    "Combobox": ttk.Combobox,

    # Advanced widgets
    "Scrollbar": ttk.Scrollbar,
    "Menu": tk.Menu,
    "Menubutton": tk.Menubutton,
    "Notebook": ttk.Notebook,
    "Treeview": ttk.Treeview,
    "Progressbar": ttk.Progressbar,
    "Separator": ttk.Separator
}

class ItemManager:
    def __init__(self, treeview_manager : TreeviewManager, design_area : DesignArea) -> None:
        self.treeview_manager = treeview_manager
        self.treeview = self.treeview_manager.treeview
        self.design_area = design_area

    def create_widget(self, widget_name : str):
        parent_id = self.treeview_manager.selected_item
        if not parent_id:
            raise ValueError("There is not any item selected to use it as a parent")

        if CONTAINER not in self.treeview.item(parent_id, "tags"):
            raise ValueError("The item selected is not a container so it can't be used as a parent")

        parent_widget = self.treeview_manager.id_to_widget.get(parent_id)

        tags = ("widget",) if widget_name not in CONTAINERS else (CONTAINER,)
        widget_id = self.treeview.insert(parent_id, "end", text=widget_name, tags=tags)

        #TODO: ADD WIDGETS TO THE DESIGN AREA WITH THE CORRESPONDING PARENT
