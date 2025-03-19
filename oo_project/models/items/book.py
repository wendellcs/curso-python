from .item_library import ItemLibrary

class Book(ItemLibrary):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self.isbn = isbn