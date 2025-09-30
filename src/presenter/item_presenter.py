from model.tree_model import TreeModel
from presenter.tree_presenter import TreeviewPresenter
from view.design_area import DesignArea
from view.tree_panel import CONTAINER

import tkinter as tk
from tkinter import ttk

from .consts import CONTAINERS, WIDGET_CLASSES

class ItemPresenter:
    def __init__(self, treeview_manager: TreeviewPresenter, design_area: DesignArea, tree_model: TreeModel):
        self.treeview_manager = treeview_manager
        self.treeview = self.treeview_manager.treeview
        self.design_area = design_area
        self.tree_model = tree_model

    def create_widget(self, widget_name: str):
        parent_id = self.tree_model.get_selected_item()
        if not parent_id:
            raise ValueError("No parent item selected.")

        if CONTAINER not in self.treeview.item(parent_id, "tags"):
            raise ValueError("Selected item is not a container.")


        tags = ("widget",) if widget_name not in CONTAINERS else (CONTAINER,)
        widget_id = self.treeview.insert(parent_id, "end", text=widget_name, tags=tags)
        parent_widget = self.tree_model.get_widget(parent_id)

        # TODO: Add widget to design area with appropriate parent





