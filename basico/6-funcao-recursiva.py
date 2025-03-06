# 1 - Fatorial de um número

def factorial(num):
    if num == 1:
        return 1
    
    return (num * factorial(num - 1))

number = int(input("Digite um número para o fatorial: \n -------> "))
print(f"O fatorial de {number} é: {factorial(number)}")

# Soma total de um número

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
    
number2 = int(input("Digite um número para a soma: \n -------> "))
print(f"O soma total de {number2} é: {total_sum(number2)}")