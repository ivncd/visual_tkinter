import tkinter as tk
from tkinter import ttk

class WidgetsFrame(ttk.Frame):
    def __init__(self, parent : tk.Misc, **kwargs):
        super().__init__(parent, **kwargs)

        self.WIDGETS_DICT = {
            "Containers": ["Frame", "LabelFrame", "Canvas"], # "PanedWindow", "Toplevel"],
            "Basic widgets": ["Button", "Label", "Entry", "Text", "Message"],
            "Selection and input": ["Checkbutton", "Radiobutton", "Spinbox", "Listbox", "Scale", "Combobox"],
            "Advanced widgets": ["Scrollbar", "Menu", "Menubutton", "Notebook", "Treeview", "Progressbar", "Separator"]
        }

        self._setup_layout()

    def _show_menu(self):
        x = self.button_add_widget.winfo_rootx() + self.button_add_widget.winfo_width()
        y = self.button_add_widget.winfo_rooty() + self.button_add_widget.winfo_height()
        self.menu.tk_popup(x, y)
        

    def setup_menu(self, function):
        self.button_add_widget = ttk.Button(self, text="Add widget", command=self._show_menu)
        self.button_add_widget.grid(row=0, column=0, sticky="nswe")

        self.menu = tk.Menu(self, tearoff=0)

        for category, widget_names in self.WIDGETS_DICT.items():
            submenu = tk.Menu(self.menu, tearoff=0)
            for name in widget_names:
                submenu.add_command(label=name, command=lambda n=name: function(n))

            self.menu.add_cascade(label=category, menu=submenu)


    def _setup_layout(self):
        self.columnconfigure(0, weight=1)


