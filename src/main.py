from ui.main_window import MainWindow 
from core.main_controller import MainController


window = MainWindow()
MainController(window)
window.mainloop()
