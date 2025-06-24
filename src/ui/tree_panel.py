import tkinter as tk
from tkinter import ttk

from .components import EditableTreeview
from core.treeview_manager import TreeviewManager

class WidgetsFrame(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)

        self.WIDGETS_DICT = {
            "Window and containers": ["Window", "Frame", "LabelFrame", "Canvas", "PanedWindow", "Toplevel"],
            "Basic widgets": ["Button", "Label", "Entry", "Text", "Message"],
            "Selection and input": ["Checkbutton", "Radiobutton", "Spinbox", "Listbox", "Scale", "Combobox"],
            "Advanced widgets": ["Scrollbar", "Menu", "Menubutton", "Notebook", "Treeview", "Progressbar", "Separator", "Sizegrip"]
        }

        self._setup_layout()
        self._setup_widgets()

    def _show_menu(self):
        x = self.button_add_widget.winfo_rootx() + self.button_add_widget.winfo_width()
        y = self.button_add_widget.winfo_rooty() + self.button_add_widget.winfo_height()
        self.menu.tk_popup(x, y)
        

    def _setup_widgets(self):
        self.button_add_widget = ttk.Button(self, text="Add widget", command=self._show_menu)
        self.button_add_widget.grid(row=0, column=0, sticky="nswe")

        self.menu = tk.Menu(self, tearoff=0)

        for category, widget_names in self.WIDGETS_DICT.items():
            submenu = tk.Menu(self.menu, tearoff=0)
            for name in widget_names:
                submenu.add_command(label=name)

            self.menu.add_cascade(label=category, menu=submenu)


    def _setup_layout(self):
        self.columnconfigure(0, weight=1)


class TreeFrame(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)

        self._setup_layout()
        self._setup_widgets()

    def _setup_widgets(self):
        self.tree = EditableTreeview(self)
        self.tree.heading("#0", text="WIDGETS")
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 20))

        TreeviewManager(self.tree).setup_bindings()

    def _setup_layout(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


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
