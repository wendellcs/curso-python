import random 
import os

# Gera valores aleatórios

# 1 - Selecionar um item aleátorio de uma lista

list1 = [1 , 3, 5 , 65 , 3 ,87 , 6 ,53 , 456 , 87, 23]
# print(random.choice(list1))

# 2 - Gerar um número aleatório dentro de um intervalo específico

# r1 = random.randint(0 , 10)
# print(r1)

# 3 - Seleciona um caractere aleatório de uma string

# print(random.choice('Curso Python'))

# 4 - Seleciona mais de um valor aleatório

# random.sample(sequencia, tamanho)
# print(random.sample(list1, 2)) # Sorteia dois valores da lista
# print(random.sample(list1, 4))


# 5 - Programa de sorteio

while True:
    user_choice = input('Guess a number between 0 and 10: \n ------> ')
    result = random.randint(0 , 10)

    if int(user_choice) == result:
        os.system('cls')
        print(f'Congratulations! \nYou got the right number!\nChosen number: {user_choice}')
        break
    else: 
        os.system('cls')
        print(f'Not this time...')