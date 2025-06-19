import tkinter as tk
from tkinter import ttk

CONTAINER = "container"
WIDGET = "widget"
HIGHLIGHT_CONTAIN = "highlight_contain"

class EditableTreeview(ttk.Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.entry = None

        self._dragging_item = None
        self._dragging_cursor = None
        self._highlighted_item = None 

        self.tag_configure(HIGHLIGHT_CONTAIN, background="#d0f0ff")
        self._setup_bindings()
        self._populate_example()


    def _populate_example(self):
        frame_id = self.insert("", "end", text="Frame", tags=(CONTAINER,))
        box_id = self.insert("", "end", text="VBox", tags=(CONTAINER,))
        grid_id = self.insert("", "end", text="Grid", tags=(CONTAINER,))

        self.insert(frame_id, "end", text="Label", tags=("widget",))
        self.insert(frame_id, "end", text="Button", tags=("widget",))
        self.insert(box_id, "end", text="Entry", tags=("widget",))
        self.insert(box_id, "end", text="Checkbutton", tags=("widget",))
        self.insert(grid_id, "end", text="Canvas", tags=("widget",))
        self.insert("", "end", text="Standalone Button", tags=("widget",))


    def _setup_bindings(self):
        # Edit bindings
        self.bind("<Double-1>", self._on_double_click)

        # Drag and drop bindings
        self.bind("<ButtonPress-1>", self._on_button_press)
        self.bind("<B1-Motion>", self._on_motion)
        self.bind("<ButtonRelease-1>", self._on_button_release)

    # -- EDIT METHODS --
    def _on_double_click(self, event):
        item_id = self.identify_row(event.y)
        column = self.identify_column(event.x)
        if not item_id or column != '#0':
            return

        x, y, width, height = self.bbox(item_id, column)
        if not (width and height):
            return

        value = self.item(item_id, "text")
        self.entry = tk.Entry(self)
        self.entry.place(x=int(x) + 20, y=y, width=width, height=height)
        self.entry.insert(0, value)
        self.entry.focus()

        self.entry.bind("<Return>", lambda e: self._save_edit(item_id))
        self.entry.bind("<FocusOut>", lambda e: self._cancel_edit())

        return "break"

    def _save_edit(self, item_id):
        if self.entry:
            new_value = self.entry.get()
            self.item(item_id, text=new_value)
            self.entry.destroy()
            self.entry = None

    def _cancel_edit(self):
        if self.entry:
            self.entry.destroy()
            self.entry = None

    # -- DRAG AND DROP METHODS --
    def _on_button_press(self, event):
        item = self.identify_row(event.y)
        if item:
            self._dragging_item = item

    def _on_motion(self, event):
        if not self._dragging_item:
            return

        if not self._dragging_cursor:
            self._dragging_cursor = self.config(cursor="hand2")

        # Check the item on the mouse and highlight it if there is a change.
        item_under_cursor = self.identify_row(event.y)

        is_container = CONTAINER in self.item(item_under_cursor, "tags")
        is_widget = WIDGET in self.item(item_under_cursor, "tags")

        # If item is a container you can move inside
        if is_container and item_under_cursor != self._highlighted_item:
            if self._highlighted_item:
                old_tags = list(self.item(self._highlighted_item, "tags"))
                if HIGHLIGHT_CONTAIN in old_tags: old_tags.remove(HIGHLIGHT_CONTAIN)
                self.item(self._highlighted_item, tags=tuple(old_tags))

            if item_under_cursor:
                new_tags = list(self.item(item_under_cursor, "tags"))
                if HIGHLIGHT_CONTAIN not in new_tags: new_tags.append(HIGHLIGHT_CONTAIN)
                self.item(item_under_cursor, tags=tuple(new_tags))

            self._highlighted_item = item_under_cursor


    def _on_button_release(self, event):
        self.config(cursor="")
        self._dragging_cursor = None

        if not self._dragging_item:
            return

        # Move item
        target_item = self.identify_row(event.y)
        if target_item and CONTAINER in self.item(target_item, "tags") and target_item != self._dragging_item and \
            not self._is_descendant(target_item, self._dragging_item):
            self.move(self._dragging_item, target_item, tk.END) #type: ignore

        # Remove highlight and change cursor back
        if self._highlighted_item:
            old_tags = list(self.item(self._highlighted_item, "tags"))
            if HIGHLIGHT_CONTAIN in old_tags: old_tags.remove(HIGHLIGHT_CONTAIN)
            self.item(self._highlighted_item, tags=old_tags)
            self._highlighted_item = None


    def _is_descendant(self, item, possible_ancestor):
        parent = self.parent(item)
        while parent:
            if parent == possible_ancestor:
                return True

            parent = self.parent(parent)

        return False
