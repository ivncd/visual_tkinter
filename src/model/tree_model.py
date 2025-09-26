
class TreeModel:
    def __init__(self):
        self.id_to_widget = {}
        self.selected_item : str | None = None

    def add_widget(self, item_id : str, widget) -> None:
        self.id_to_widget[item_id] = widget

    def get_widget(self, item_id : str):
        return self.id_to_widget.get(item_id)

    def set_selected_item(self, item_id):
        self.selected_item = item_id

    def get_selected_item(self):
        return self.selected_item


