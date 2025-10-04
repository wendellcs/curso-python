import sqlite3

def conecta_bd():
    conexao = sqlite3.connect('../jogos.db')
    return conexao

def adicionar_dados(jogo, ano, empresa):
    conexao = conecta_bd()
    cursor = conexao.cursor()

    cursor.execute(
        """
            INSERT INTO jogos (jogo, ano, empresa)
            VALUES (? , ? , ?)
        """,
        (jogo , ano, empresa)
    )
    conexao.commit()
    conexao.close()

def obter_jogos():
    conexao = conecta_bd()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM jogos")
    dados = cursor.fetchall()
    conexao.close()

    return dados