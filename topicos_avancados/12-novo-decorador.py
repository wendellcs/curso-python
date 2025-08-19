from decorator import my_decorator, uppercase_decorator, split_string

@my_decorator
def my_function():
    print("dentro da função")

my_function()

@uppercase_decorator
def text():
    return 'Hello, World!'

print(text())

@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())