# Decorator

# - Modificam ou extendem o comportamento de funções ou métodos de forma reutilizável.
# - Adicionam funcionalidades a funções existentes sem modificar seu código diretamente.

def my_decorator(function):
    def wrapper():
        print("Antes de executar a função")
        function()
        print("Depois de executar a função")
        
    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper