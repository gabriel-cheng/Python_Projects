"""
Exemplo
"""

lista = [1, 2, 3, 4, 9, 8, 7, 6, 5, 15, 14, 13, 12, 11, 10]
print("O que você deseja fazer? ")
print("A) Organizar a lista em ordem crescente")
print("B) Organizar a lista em ordem decrescente")
resp = input("Escolho a letra: ")

if resp == "A" or resp == "a":
    lista.sort()
    print(f"Lista organizada em ordem crescente: {lista}")
elif resp == "B" or resp == "b":
    lista.sort()
    lista.reverse()
    print(f"Lista organizada de forma decrescente: {lista}")
