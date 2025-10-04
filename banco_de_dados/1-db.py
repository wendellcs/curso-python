# Banco de dados com python

# SQLite

import sqlite3 # Módulo nativo

# 1 - Criando o banco de dados: jogos.db

conexao = sqlite3.connect('jogos.db') 
# O connect serve tanto para criar quanto para conectar em um banco de dados existente.


# 2 - Criando o cursor ( O cursor permite realizar operações dentro do DB )

cursor = conexao.cursor()

# 3 - Criando a tabela

cursor.execute(
    """
        CREATE TABLE jogos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            jogo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            empresa TEXT NOT NULL
        );
    """
)

# 4 - Fechando a conexão
conexao.close()
print('Tabela criada com sucesso!')