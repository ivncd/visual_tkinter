import tkinter as tk

from view.tree_panel import EditableTreeview, MenuEditableTreeview, HIGHLIGHT_CONTAIN, CONTAINER
from model.tree_model import TreeModel

class TreeviewPresenter:
    def __init__(self, treeview : EditableTreeview, model : TreeModel):
        self.treeview = treeview
        self.model = model

        self.menu_manager = MenuEditableTreeview(self)

        self.entry = None
        self._dragging_item = None
        self._dragging_cursor = None
        self._highlighted_item = None 

        self._setup_bindings()

    def _setup_bindings(self):
        # Menu bindings
        self.treeview.bind("<Button-3>", self._show_menu, add="+")

        # Drag and drop bindings
        self.treeview.bind("<ButtonPress-1>", self._on_button_press)
        self.treeview.bind("<B1-Motion>", self._on_motion)
        self.treeview.bind("<ButtonRelease-1>", self._on_button_release)

    def _show_menu(self, event):
        item_id = self.treeview.identify_row(event.y)
        if not item_id:
            return

        self.menu_manager.setup_commands(event, item_id)

    # -- DRAG AND DROP METHODS --
    def _on_button_press(self, event):
        item = self.treeview.identify_row(event.y)
        if item:
            self._dragging_item = item
            self.model.selected_item = item
        elif len(self.treeview.selection()) > 0: # Remove highlight when there is no selected_item
            self.treeview.selection_remove(self.treeview.selection()[0])
            self.model.selected_item = None
                

    def _on_motion(self, event):
        if not self._dragging_item:
            return

        if not self._dragging_cursor:
            self._dragging_cursor = self.treeview.config(cursor="hand2")

        # Check the item on the mouse and highlight it if there is a change.
        item_under_cursor = self.treeview.identify_row(event.y)

        # If item is a container you can move inside
        is_container = CONTAINER in self.treeview.item(item_under_cursor, "tags")
        if is_container and item_under_cursor != self._highlighted_item:
            if self._highlighted_item:
                old_tags = list(self.treeview.item(self._highlighted_item, "tags"))
                if HIGHLIGHT_CONTAIN in old_tags: old_tags.remove(HIGHLIGHT_CONTAIN)
                self.treeview.item(self._highlighted_item, tags=tuple(old_tags))

            if item_under_cursor:
                new_tags = list(self.treeview.item(item_under_cursor, "tags"))
                if HIGHLIGHT_CONTAIN not in new_tags: new_tags.append(HIGHLIGHT_CONTAIN)
                self.treeview.item(item_under_cursor, tags=tuple(new_tags))

            self._highlighted_item = item_under_cursor


    def _on_button_release(self, event):
        self.treeview.config(cursor="")
        self._dragging_cursor = None

        if not self._dragging_item:
            return

        # Move item
        target_item = self.treeview.identify_row(event.y)
        if target_item and CONTAINER in self.treeview.item(target_item, "tags") and target_item != self._dragging_item and \
            not self._is_descendant(target_item, self._dragging_item):
            self.treeview.move(self._dragging_item, target_item, tk.END)

        # Remove highlight and change cursor back
        if self._highlighted_item:
            old_tags = list(self.treeview.item(self._highlighted_item, "tags"))
            if HIGHLIGHT_CONTAIN in old_tags: old_tags.remove(HIGHLIGHT_CONTAIN)
            self.treeview.item(self._highlighted_item, tags=old_tags)
            self._highlighted_item = None


    def _is_descendant(self, item, possible_ancestor):
        parent = self.treeview.parent(item)
        while parent:
            if parent == possible_ancestor:
                return True

            parent = self.treeview.parent(parent)

        return False

    # -- MENU METHODS --
    def _save_edit(self, item_id):
        if self.entry:
            new_value = self.entry.get()
            self.treeview.item(item_id, text=new_value)
            self.entry.destroy()
            self.entry = None

    def _cancel_edit(self):
        if self.entry:
            self.entry.destroy()
            self.entry = None


    def rename_item(self, event):
        self._cancel_edit() # Remove last entry if it hasn't been deleted

        item_id = self.treeview.identify_row(event.y)
        column = self.treeview.identify_column(event.x)
        if not item_id or column != '#0':
            return

        x, y, width, height = self.treeview.bbox(item_id, column)
        if not (width and height):
            return

        value = self.treeview.item(item_id, "text")
        self.entry = tk.Entry(self.treeview)
        self.entry.place(x=int(x) + 15, y=y, width=width, height=height)
        self.entry.insert(0, value)
        self.entry.focus()

        self.entry.bind("<Return>", lambda _: self._save_edit(item_id))
        self.entry.bind("<FocusOut>", lambda _: self._cancel_edit())

    def move_item(self, item_id, index_dif):
        parent = self.treeview.parent(item_id)
        siblings = self.treeview.get_children(parent)
        index = siblings.index(item_id)

        if index > 0 and index_dif == -1 or index < len(siblings) - 1 and index_dif == 1:
            self.treeview.move(item_id, parent, index + index_dif)

    # TODO: Add confirmation window with "do not show again" checkbox
    def delete_item(self, item_id):
        self.treeview.delete(item_id)
        if self.model.selected_item == item_id:
            self.model.selected_item = None



