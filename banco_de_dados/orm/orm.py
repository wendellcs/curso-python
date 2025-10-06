# ORM -> Mapeamento objeto relacional

# Ferramenta que me aproxima de um banco de dados relacional com a programação orientada a objetos. 
# Com isso não é necessário código SQL.

from sqlalchemy import create_engine, Column, Integer, String, Float 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db' , echo = True) 
Base = declarative_base()

class Jogo(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key=True)
    jogo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    empresa = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

# Cria a tabela no banco de dados
Base.metadata.create_all(engine)

# Inserir dados

def adiciona_jogo(jogo , ano , empresa , preco):
    Session = sessionmaker(bind = engine)
    session = Session()
    jogo = Jogo(jogo = jogo, ano = ano , empresa = empresa, preco = preco)
    session.add(jogo)
    session.commit()
    session.close()

# adiciona_jogo('Minecraft' , 2009, 'Mojang' , 149.90)

def atualiza_jogo(id , jogo = None , ano = None , empresa = None, preco = None):
    Session = sessionmaker(bind = engine)
    session = Session()
    jogo_atualizar = session.query(Jogo).filter_by(id = id).first()
    if jogo_atualizar:
        if jogo is not None:
            jogo_atualizar.jogo = jogo

        if ano is not None:
            jogo_atualizar.ano = ano

        if empresa is not None:
            jogo_atualizar.empresa = empresa

        if preco is not None:
            jogo_atualizar.preco = preco

        session.commit()
    session.close()

# atualiza_jogo(1 , 'CS2', 2022, 'Valve' , 90.00)

# Excluir dados

def deleta_jogo(id):
    Session = sessionmaker(bind = engine)
    session = Session()
    jogo_atualizar = session.query(Jogo).filter_by(id = id).first()
    if jogo_atualizar:
        session.delete(jogo_atualizar)

    session.commit()
    session.close()

# deleta_jogo(1)