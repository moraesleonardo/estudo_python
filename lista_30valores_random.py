# crie uma lista de 30 valores aleatórios entre 1 e 50 usando a biblioteca random

import random
list_aleatoria = [random.randint(1, 50) for i in range(30)]

print(list_aleatoria)

# plote um histograma do vetor aleatório criado

import matplotlib.pyplot as plt

plt.hist(list_aleatoria)
plt.show()

# calcule a média

media = sum(list_aleatoria)/len(list_aleatoria)
print(media)

import statistics as stats
print(stats.mean(list_aleatoria))

# calcule a mediana

import statistics as stats
mediana = stats.median(list_aleatoria)
print(stats.median(list_aleatoria))

# calcule a moda

from collections import Counter
moda = Counter(list_aleatoria)
print(Counter(list_aleatoria))

# calcule o desvio padrão

import statistics as stats
dev_pad = stats.pstdev(list_aleatoria)
print(stats.pstdev(list_aleatoria))

# calcule a variância

import statistics as stats
var = stats.pvariance(list_aleatoria)
print(stats.pvariance(list_aleatoria))

inf = {"media": media, "mediana": mediana, "moda": moda, "desvio padrão": dev_pad, "variância": var}
print(inf)

arquivo = open("informacoes.txt", "w")
arquivo.write(str(inf))
arquivo.close()