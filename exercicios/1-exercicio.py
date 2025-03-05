# 1 - Escreva um programa que lê dois nomes e retorne uma string
#     formatada no formato "ÚltimoNome, PrimeiroNome".

# 2 - Inverta a ordem das palavras em uma string fornecida.

# 3 - Verifique se uma string fornecida é um palíndromo.

# Exercicio 1:

primeiroNome = input("Insira um nome")
ultimoNome = input("Insira outro nome")

print(ultimoNome, ',' , primeiroNome)

# Exercicio 2: 

frase = 'Aprofundando os meus conhecimentos em python'
novaFrase = frase.split(' ')
novaFrase.reverse()
print(' '.join(novaFrase))

# Exercicio 3:

palavra = 'Natan'
palavraOriginal = palavra.lower()

print(palavra[::-1].lower() == palavraOriginal )
