from ui.main_window import MainWindow, BUTTON_PADDING, COLLAPSED_TREE_WIDTH, DEFAULT_TREE_WIDTH
from core.treeview_manager import TreeviewManager
from core.item_manager import ItemManager

class MainController:
    def __init__(self, main_view : MainWindow) -> None:
        self.main_view = main_view

        self._setup_controllers()
        self._setup_binds()

    def _setup_controllers(self):
        treeview = self.main_view.tree_panel.frame_tree.tree
        treeview_manager = TreeviewManager(treeview)
        treeview_manager.setup_bindings()

        item_manager = ItemManager(treeview_manager, self.main_view.design_area)

        # Setup menu so that it can create widgets when pressing
        self.main_view.tree_panel.frame_widgets.setup_menu(item_manager.create_widget)

    # -- METHODS TO COLLAPSE TREE PANEL MENU --
    def _setup_binds(self):
        self.main_view.button_collapse.configure(command=self._collapse_tree_panel)

    def _collapse_tree_panel(self):
        new_tree_width = COLLAPSED_TREE_WIDTH if not self.main_view.collapsed else DEFAULT_TREE_WIDTH
        self.main_view.tree_panel.place(x=0, y=0, width=new_tree_width, relheight=1.0)
        self.main_view.button_collapse.configure(text='>' if not self.main_view.collapsed else '<')
        self.main_view.button_collapse.place(x=new_tree_width + BUTTON_PADDING, rely=0.5, height=50, width=20, anchor="e")

        self.main_view.collapsed = not self.main_view.collapsed
