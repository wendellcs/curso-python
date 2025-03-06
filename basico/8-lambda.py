# Função de potência de um número

power = lambda num: num ** 2
print(power(5))
print(power(9))

# Função que verifica se um número é par

is_even = lambda num:num % 2 == 0

number = int(input("Verifique se o número é par:\n -----> "))
print(f"O número {number} é: {"par" if is_even(number) else "impar"}")

# Função que divide um número por outro

div_num = lambda x, y: x / y

print(div_num(3 , 8))
print(div_num(6 , 3))
print(div_num(50 , 10))

# Função que inverte uma string

reverse_string = lambda s: s[::-1]

print(reverse_string("Python"))
print(reverse_string("JavaScript"))
print(reverse_string("Assembly"))


# Funcionalidade relacionada aos filmes

movie_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

ratings = {
    "Titanic": [8.5 , 7.8 , 8.0],
    "The Godfather": [6.7 , 9.0 , 9.5],
    "Inception": [4.1, 8.1 , 5.8],
    "Jurassic Park": [9.1, 4.9 , 5.0]
}

# Função para calcular a média de avaliações de um filme

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f"A média de avaliação do filme Titanic: {average_rating("Titanic")}")

# Função que verifica se um filme esta na lista

check_movie = lambda movie_name: movie_name in movie_list

print(check_movie("Titanic"))

# Função para recomendar um filme com base na avaliação média

recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"
print(f"{recommend_movie("Titanic")}")