"""
    *args - Utilizamos quando não sabemos quantos argumentos uma função receberá.

        -> Os argumentos são passados como uma tupla.

    **kwargs - Além dos valores, podemos passar também chaves para cada argumento.

        -> Os argumentos são passados como um dicionário.

"""

# Somando números

def sum(*num):
    sum_total = 0

    for n in num:
        sum_total += n

    print(f"A soma é {sum_total}")

sum(5 , 6 , 7 , 8 , 4 , 87, 43, 2)


# Apresentação de cursos

def presentation(**data):
    print("-" * 50)
    print("\n")
    for key , value in data.items():
        print(f"{key} - {value}")

    print("\n")

print("\n ---> Lista de cursos <--- \n")

presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")