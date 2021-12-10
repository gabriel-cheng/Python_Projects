"""
Ordered Dict - Dicionário ordenado
- Em um dicionário comum, a ordem de inserção dos elementos não garante a ordem na impressão
- Quando você vai adicionando elementos no dicionários, ele se organiza automaticamente.

dicio = {'name': 'Gabriel', 'name2': 'Rafael'}
print(dicio)
print(type(dicio))

for chave, valor in dicio.items():
    print(f'chave = {chave}, valor = {valor}')

dicio['lindo'] = 'Eu sou lindo'

print(dicio)
"""
from collections import OrderedDict

dicio = OrderedDict({'a': 'Gabriel', 'b': 'Rafael'})
"""É um dicionário que nos garante a ordem de inserção de elementos"""

for chave, valor in dicio.items():
    print(f'Chave = {chave}, valor = {valor}')

"""
Entendendo a diferença de um dicionário comum
"""
# Para um dicionário comum, a ordem não importa, somente os valores
dicium = {'a': 1, 'b': 2}
dicidois = {'b': 2, 'a': 1}

print(dicium == dicidois)

# No OrderedDict a ordem dos elementos também define a igualdade de ambos
dicium = OrderedDict({'a': 1, 'b': 2})
dicidois = OrderedDict({'b': 2, 'a': 1})

# print(dicium == dicidois) -> Para adicionar elementos é normal

dicium['c'] = 3
print(dicium)

























