import sqlite3

conexao = sqlite3.connect('jogos.db')
cursor = conexao.cursor()

# 4 - Atualizando dados

id = 3

cursor.execute(
    """
        UPDATE jogos SET jogo = ?
        WHERE id = ?
    """,
    ("CS2" , id)
)

conexao.commit()
print('Dados atualizados com sucesso!')