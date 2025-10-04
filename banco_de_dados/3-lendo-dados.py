import sqlite3

conexao = sqlite3.connect('jogos.db')
cursor = conexao.cursor()

# 3 - Lendo dados

dados = cursor.execute(" SELECT * FROM jogos ")

# fetchall() -> Usamos para pegarmos os dados corretamente.
print(dados.fetchall())

conexao.close()