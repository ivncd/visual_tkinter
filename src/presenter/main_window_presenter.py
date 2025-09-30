from view.main_window import MainWindow, BUTTON_PADDING, COLLAPSED_TREE_WIDTH, DEFAULT_TREE_WIDTH
from model.main_window_model import MainWindowModel

from .tree_presenter import TreeviewPresenter
from .item_presenter import ItemPresenter
from view.window import CreateProjectWindow

from utils.window_utils import center_window

class MainWindowPresenter:
    def __init__(self, main_view: MainWindow, model: MainWindowModel):
        self.view = main_view
        self.model = model

        self._setup_presenters()
        self._setup_binds()
        self.view.setup_menu(self.create_window)

    def _setup_presenters(self):
        treeview = self.view.tree_panel.frame_tree.tree

        self.treeview_presenter = TreeviewPresenter(treeview, self.model.tree_model)
        self.item_presenter = ItemPresenter(self.treeview_presenter, self.view.design_area, self.model.tree_model)

        self.view.tree_panel.frame_widgets.setup_menu(self.item_presenter.create_widget)

    def create_window(self) -> None:
        create_toplevel = CreateProjectWindow(self.view)
        center_window(create_toplevel)

    # -- SETUP COLLAPSE ACTION TO TREE PANEL --
    def _setup_binds(self):
        self.view.button_collapse.configure(command=self._collapse_tree_panel)

    def _collapse_tree_panel(self):
        collapsed = self.model.collapsed
        new_tree_width = COLLAPSED_TREE_WIDTH if not collapsed else DEFAULT_TREE_WIDTH

        self.view.tree_panel.place(x=0, y=0, width=new_tree_width, relheight=1.0)
        self.view.button_collapse.configure(text='>' if not collapsed else '<')
        self.view.button_collapse.place(x=new_tree_width + BUTTON_PADDING, rely=0.5, height=50, width=20, anchor="e")

        self.model.collapsed = not collapsed
