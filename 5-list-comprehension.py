# 1 - Listar valores de 0 à 10 que sejam menores do que 4.

# Com for:

# for i in range(10):
#     if i < 4: 
#         print(i)

# Com list comprehension:

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)


# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 2 - Filmes que possuem a letra 'e' no título.

moviesWithE = [movie for movie in moviesList if "e" in movie.lower()]
print(moviesWithE)

# 3 - Filtrar filmes 

allMoviesButTitanic = [movie for movie in moviesList if movie != "Titanic"]
print(allMoviesButTitanic)

# 4 - Encontrando um filme pelo nome

while True:
    searchName = input("Digite o nome de um filme para buscar na lista ( ou sair para encerrar ) \n -----> ")

    if searchName.lower() == "sair":
        print("Programa encerrado")
        break 

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]

    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome: {searchName}")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome: {searchName}")