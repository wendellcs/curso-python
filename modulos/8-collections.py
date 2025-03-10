from collections import Counter, namedtuple , deque 
from operator import itemgetter

# 1 - Lista de frutas ( Contagem )

fruits = ['Maçã' , 'Banana' , 'Uva' , 'Pêra' , 'Banana' , 'Uva', 'Maçã' , 'Laranja' , 'Abacaxi', 'Tangerina' , 'Uva', 'Pêra' , 'Banana']

print(Counter(fruits)) # Faz a contagem de um determinado item

# 2 - Utilizando tupla nomeada

game = namedtuple('game' , ['name', 'price', 'note'])
g1 = game('Fifa 23' , 100.00 , 8.8)
g2 = game('Resident Evil 4 Remake' , 350.00 , 10.0)

print(g1)
print(g2.name)

# Ordenando dicionários

students = {
    'Pedro': 23,
    'Ronaldo': 26,
    'João': 18,
    'Janaíra': 22           
}

a = sorted(students.items(), key = itemgetter(0)) # Posição 0 é a chave, 1 o valor.
print(a)

# Utilizando uma fila em ambas extremidades

deq = deque([20, 40 , 60 , 80])
deq.appendleft(10)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)