# Programa principal

import math_operations as ma # Importa todo o módulo ( o "as" é um apelido para o módulo )
from math_operations import multiply, divide # Importa funções específicas

import string_utils as strUlt

print(ma.sum(78 , 45))
print(ma.subtract(78 , 45))

print(multiply(78 , 45))
print(divide(78 , 45))

print(strUlt.capitalize("python"))
print(strUlt.count("python"))
print(strUlt.reverse("python"))