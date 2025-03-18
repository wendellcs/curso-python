from models.rating import Rating

# Encapsulation - Refers to a bundling ( group ) of attributes and methods that operate on the data 
# into a class. 
# It also retricts direct acces to some components, which helps protect the integrity of the data.

class Library:
    librarys = []

    def __init__(self, name):
        self.name = name
        # A single underscore can still be accesed outside the class, since it is merely a convention for the programmers.
        # Double underscore refers to the private method, which can not be accessed outside the class.
        # self._active = False 
        self._active = False
        self._rating = []

        Library.librarys.append(self) # self is a reference for the object.

    def __str__ (self):
        return self.name # Returns the library's name
    
    # When a method is defined using the @classmethod decorator, the method can not
    # be accessed by a instance of the class.
    @classmethod 
    def list_librarys(cls):
        print('-'*30)
        print(f"{'Library name'.ljust(15)} | {'Rating'.ljust(25)} | Status\n")
        for library in Library.librarys:
            print(f'{library.name.ljust(15)} | {str(library.rating_average).ljust(25)} | {library.active}')
        print('-'*30)

    def toggle_state(self): # Example of set method
        self._active = not self._active

    # It is recommended to use @property for get methods
    @property 
    def active(self):
        return 'Activated' if self._active else 'Deactivated'
    
    def receive_rating(self, client, note):
        rating = Rating(client, note)
        self._rating.append(rating)

    @property
    def rating_average(self):
        if not self._rating:
            return '-'
        
        total_sum = sum(rating._note for rating in self._rating)
        average = round(total_sum / len(self._rating), 1)
        return average
