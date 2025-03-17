from models.library import Library

city_library = Library("City's Library")
city_library.__active = True # Won't have effect, since this is a private method.
city_library.toggle_state()

city_library.receive_rating('João', 7.9)
city_library.receive_rating('Marcela', 5.3)

mall_library = Library("Mall's Library")

# print(vars(city_library))
# vars() - Returns the __dict__ attribute of an object ( dictionary.__dict__ ).
# The __dict__ attribute is a dictionary containing the object's changeable attributes.

def main():
    Library.list_librarys()

# Chechs if this file is being directly executed or imported.
if __name__ == '__main__':
    main() # Executes if the script is run directly.

# __name__ is an especial variable
