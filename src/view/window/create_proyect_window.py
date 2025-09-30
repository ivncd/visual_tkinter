import tkinter as tk
from tkinter import ttk

class CreateProjectWindow(tk.Toplevel):
    def __init__(self, main_window : tk.Tk,  **kwargs) -> None:
        super().__init__(main_window, **kwargs)

        self._setup_layout()
        self._setup_widgets()

    def _setup_layout(self) -> None:
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def _setup_widgets(self) -> None:

        dimensions_label = tk.Label(self, text="Dimensions", anchor=tk.CENTER)   
        dimensions_label.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="WIDTH:").grid(row=1, column=0, pady=5, padx=10)
        ttk.Label(self, text="HEIGHT:").grid(row=2, column=0, pady=5, padx=10)

        self.entry_width = ttk.Entry(self)
        self.entry_width.grid(row=1, column=1, pady=5, padx=10)

        self.entry_height = ttk.Entry(self)
        self.entry_height.grid(row=2, column=1, pady=5, padx=10)

        self.button_create = ttk.Button(self, text="Create")
        self.button_create.grid(row=3, column=0, columnspan=2, sticky="sew", pady=5, padx=10)

# TEST SETUP
if __name__ == "__main__":
    window = tk.Tk()
    CreateProjectWindow(window)
    window.mainloop()
