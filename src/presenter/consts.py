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
