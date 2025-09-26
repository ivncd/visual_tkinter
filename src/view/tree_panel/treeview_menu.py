from typing import TYPE_CHECKING

from .editable_treeview import EditableTreeview

if TYPE_CHECKING:
    from presenter.tree_presenter import TreeviewPresenter

class MenuEditableTreeview:
    def __init__(self, presenter : 'TreeviewPresenter'):
        self.presenter = presenter;
        self.treeview = presenter.treeview;
        self.menu = self.treeview.menu

    def setup_commands(self, event, item_id):
        self.menu.delete(0, "end")
        self.treeview.selection_set(item_id)

        self.menu.add_command(label="Move up", command=lambda: self.presenter.move_item(item_id, -1))
        self.menu.add_command(label="Move down", command=lambda: self.presenter.move_item(item_id, 1))
        self.menu.add_separator()
        self.menu.add_command(label="Rename", command=lambda: self.presenter.rename_item(event))
        self.menu.add_command(label="Delete", command=lambda: self.presenter.delete_item(item_id))
        self.menu.add_command(label="Properties")

        self.menu.tk_popup(event.x_root, event.y_root)
