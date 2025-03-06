moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# Iterando valores de uma lista de filmes usando while

# index = 0
# while index < len(moviesList):
#     print(moviesList[index])
#     index += 1

# Deixando o usuário aumentar os itens da lista

stop = False
while True: 
    if not stop:
        newMovie = input("Insira um novo filme: ")
        moviesList.append(newMovie)
        print(moviesList)
        keepGoing = input("Parar? \n 1 - Sim \n 2 - Não \n ----> ")
        stop = True if keepGoing == "1" else False
    else: 
        print(f"Essa é sua lista atualizada: \n {moviesList}")
        print("Encerrando o programa...")
        break
    