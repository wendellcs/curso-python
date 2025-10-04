import sqlite3

conexao = sqlite3.connect('jogos.db')
cursor = conexao.cursor()

# 2 - Inserindo dados

cursor.execute(
    """
        INSERT INTO jogos(jogo , ano , empresa)
        VALUES ('CS@' , 2022 , 'Valve')
    """
)

conexao.commit()
conexao.close()

print('Dados adicionados na tabela!')