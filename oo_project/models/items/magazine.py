from .item_library import ItemLibrary

class Magazine(ItemLibrary):
    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.edition = edition