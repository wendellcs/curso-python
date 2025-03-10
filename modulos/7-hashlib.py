# Módulo para trabalhar com a criptografia de textos

import hashlib

# 1 - Verificar os algoritmos disponiveis

print(hashlib.algorithms_available)

# 2 - Verificar os algoritmos de acordo com o SO

print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256

algorithm = hashlib.sha256()
print(algorithm.digest())

msg = 'A melhor forma de prever o futuro é criá-lo'.encode()
algorithm.update(msg)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5

md5 = hashlib.md5()
md5.update(msg)
print(md5.hexdigest())