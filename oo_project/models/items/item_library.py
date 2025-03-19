from abc import ABC, abstractmethod

class ItemLibrary(ABC):
    def __init__(self, title, author , price):
        self._title = title 
        self._author = author
        self._price = price

    @abstractmethod
    def apply_discount(): # Different books can have different discounts
        pass

# Abstract class - A class which cannot be instantiated on its own and is designed to be a 
# blueprint of other class.

# Abstract methods - Abstract methods are methods declared in an abstract class that do 
# not have an implementation in the abstract class itself. They are meant to be overridden 
# in the derived (or child) classes.