"""
Entendendo o método de ordenação Insertion Sort em Python
"""


def insertion_sort(lista):
    tamanhoLista = len(lista)
    for i in range(1, tamanhoLista): # Itera com elementos dentro da lista começando do segundo elemento
        chave = lista[i] # Chave recebe lista[na posição de i]
        j = i - 1 # Informa que a variável j se inicia no primeiro elemento da lista
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave





