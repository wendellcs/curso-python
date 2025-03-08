import statistics

# Média 

print(statistics.mean([3 , 5 , 6 , 2 , 4 , 7 , 10]))

# Mediana 

print(statistics.median([1 , 2 , 4 , 8 , 9]))
print(statistics.median([1 , 2 , 3 , 7 , 8 , 9]))

# Moda 

print(statistics.mode([2 , 5 , 6 , 2 , 3 , 8 , 9 , 4 , 5 , 7]))

# Desvio padrão

'''
    Quanto mais próximo de 0 for o desvio padrão, 
    significa que os dados do conjunto estão menos dispersos
'''

print(statistics.stdev([1 , 1.5 , 2 , 2.5 , 3 , 3.5 , 4 , 4.5]))