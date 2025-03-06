filme = {
    "nome": "Até o último homem",
    "ano": 2012,
    "nota": "8/10"
}

# Métodos de dicionário

# Pegar elementos de um dicionário

print(filme["nome"])
print(filme.get("nome"))

# Buscar as chaves de um dicionario

print(filme.keys())

# Buscar os valores do dicionário

print(filme.values())

# Busca os itens com chave e valores

print(filme.items())

# Adicionar nova informação ao dicionário

filme["diretor"] = "Alguém aí"
print(filme)

# Atualizar algo em um dicionário

filme.update({"nota": "8.5/10"})
print(filme)

# Remover item no dicionário

filme.pop("diretor")
print(filme)


# Dicionários aninhados

filmsDict = {
    "Até o último homem": {
        "ano": 2012,
        "nota": "8/10"
    },
    "Corações de Ferro": {
        "ano": 2016,
        "nota": "8.5/10"
    },
    "Algum aí": {
        "ano": 1999,
        "nota": "10/10"
    }

}

import pprint

pp = pprint.PrettyPrinter(depth=5)

pp.pprint(filmsDict)
