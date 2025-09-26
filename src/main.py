from view.main_window import MainWindow 
from presenter.main_window_presenter import MainWindowPresenter
from model.main_window_model import MainWindowModel


window = MainWindow()
model = MainWindowModel()
MainWindowPresenter(window, model)
window.mainloop()
