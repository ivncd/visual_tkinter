from .tree_model import TreeModel
from .item_model import ItemModel

class MainWindowModel:
    def __init__(self):
        self.collapsed = False
        self.tree_model = TreeModel()
        self.item_model = ItemModel()
