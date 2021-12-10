"""
Algoritmo de um mercado

- Mercado com diversos produtos, onde o usuário deverá informar o nome dos produtos que deseja
comprar e o produto escolhido será adicionado ao carrinho, onde o carrinho será informado com todos os produtos
contidos, incluindo uma contagem.
"""

produtos = [
    "Tomate",
    "Laranja",
    "Alface",
    "Limão",
    "Banana",
    "Arroz",
    "Feijão",
    "Açúcar",
    "Playstation 4"
]

carrinho = []
cliente = " "

print(produtos)
while cliente != 'sair':
    cliente = input("Desejo comprar...: ")
    carrinho.append(cliente)
print(carrinho)
for indice, produtos in enumerate(carrinho):
    print(indice, produtos)









