import tkinter as tk
from tkinter import ttk

from ui.components import EditableTreeview, CONTAINER, HIGHLIGHT_CONTAIN

class TreeviewManager:
    def __init__(self, treeview : EditableTreeview):
        self.treeview = treeview
        self.menu_manager = MenuManager(self.treeview, self)
        self.id_to_widget = {}

        self.entry = None
        self.selected_item = None
        self._dragging_item = None
        self._dragging_cursor = None
        self._highlighted_item = None 

    def setup_bindings(self):
        # Menu bindings
        self.treeview.bind("<Button-3>", self.menu_manager.show_menu, add="+")

        # Drag and drop bindings
        self.treeview.bind("<ButtonPress-1>", self._on_button_press)
        self.treeview.bind("<B1-Motion>", self._on_motion)
        self.treeview.bind("<ButtonRelease-1>", self._on_button_release)

    # -- EDIT METHODS --
    def _rename_item(self, event):
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

        self.entry.bind("<Return>", lambda e: self._save_edit(item_id))
        self.entry.bind("<FocusOut>", lambda e: self._cancel_edit())

        return "break"

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

    # -- DRAG AND DROP METHODS --
    def _on_button_press(self, event):
        item = self.treeview.identify_row(event.y)
        if item:
            self._dragging_item = item
            self.selected_item = item
        elif len(self.treeview.selection()) > 0: # Remove highlight when there is no selected_item
            self.treeview.selection_remove(self.treeview.selection()[0])
            self.selected_item = None
                

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


# TODO: Duplicate method for the menu
class MenuManager:
    def __init__(self, treeview : EditableTreeview, manager : TreeviewManager):
        self.treeview = treeview
        self.manager = manager
        self.menu = self.treeview.menu


    def _setup_commands(self, event, item_id):
        self.treeview.selection_set(item_id)
        self.treeview.menu.add_command(label="Move up", command=lambda: self._move_item(item_id, -1))
        self.menu.add_command(label="Move down", command=lambda: self._move_item(item_id, 1))
        self.menu.add_separator()
        self.menu.add_command(label="Rename", command=lambda: self.manager._rename_item(event))
        self.menu.add_command(label="Delete", command=lambda: self._delete_item(item_id))
        self.menu.add_command(label="Properties")

    def _clear_menu(self):
        self.menu.delete(0, "end")

    def show_menu(self, event):
        item_id = self.treeview.identify_row(event.y)
        if not item_id:
            return

        self._clear_menu()
        self._setup_commands(event, item_id)
        self.menu.tk_popup(event.x_root, event.y_root)

    # -- MENU METHODS --
    # TODO: Add confirmation window with "do not show again" checkbox
    def _delete_item(self, item_id):
        self.treeview.delete(item_id)
        if self.manager.selected_item == item_id:
            self.manager.selected_item = None

    def _move_item(self, item_id, index_dif):
        parent = self.treeview.parent(item_id)
        siblings = self.treeview.get_children(parent)
        index = siblings.index(item_id)

        if index > 0 and index_dif == -1 or index < len(siblings) - 1 and index_dif == 1:
            self.treeview.move(item_id, parent, index + index_dif)
