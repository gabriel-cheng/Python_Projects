"""
Revisão de Conteúdo
"""
from collections import Counter
# Lista

user = " "
lista = []

while user != "sair":
    user = input("Informe os nomes desejados...: ")
    lista.append(user)
#   lista = lista + list(user) - Usar isso faz com que seja impresso de letra em letra
if user == 'sair':
    lista.pop()
    desejo = input('Deseja ver quantos itens se repetiram..?')
    if desejo == 'sim':
        counter = Counter(lista)
        print(counter.most_common())
    else:
        for indice, nome in enumerate(lista):
            print(indice, nome)






























