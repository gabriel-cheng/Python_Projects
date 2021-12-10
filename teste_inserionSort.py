"""
Testando o insertion sort
"""
# Versão outras linguagens
import random
from insertion_sort import insertion_sort

randomLista = random.sample(range(1, 1000), 25) # Variável randomLista recebe 42 nº aleatórios entre 1 ~ 1000

print(f"Normal: {randomLista}")

insertion_sort(randomLista) # Aplicando a função criada
print("Ordenado: ", end="")
print(randomLista, "\n \n \n")

##############################################################################################################
# Versão Python

randomLista2 = random.sample(range(1, 1000), 25)
print(f"Normal {randomLista2}")
randomLista2.sort()
print("Ordenado:", randomLista2)

