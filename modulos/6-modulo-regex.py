# Expressões regulares - Regex

text = 'Python é uma das linguagens de programação mais utilizadas do mundo'

# Índice inicial e final de palavras.
# o r siginifica uma raw string ( string bruta )

import re 

match = re.search(r'linguagens', text)
print(f'Índice inicial: {match.start()}')
print(f'Índice final: {match.end()}')

# Buscando o índice que possui o pornto

site = 'https://youtube.com'

match = re.search(r'\.' , site)
print(match)

# Buscar uma lista de caracteres dentro de uma frase

pattern = '[g-m]'
result = re.findall(pattern, text)
print(result)

# Verificando o inicio de uma string 

rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']

for f in phrases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print('Não corresponde')


# Verificando o final de uma string

rule = r'!$'
phrase = 'O dia está lindo!'
match = re.search(rule, phrase)

if match:
    print('Sim, corresponde')
else: 
    print('Não corresponde')