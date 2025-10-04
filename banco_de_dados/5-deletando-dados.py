import sqlite3

conexao = sqlite3.connect('jogos.db')
cursor = conexao.cursor()

# 4 - Deletando dados

id = 3
# Para excluir mais de um registro, passe uma tupla com os ids desejados. EX: id = (1 , 2, ... N)

cursor.execute(
    """
        DELETE FROM jogos
        WHERE id = ?
    """,
    (id,) # A vírgula garante que é uma tupla
)

conexao.commit()
print('Dados excluídos com sucesso!')