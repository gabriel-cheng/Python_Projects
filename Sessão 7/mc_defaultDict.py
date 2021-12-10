"""
Módulo Collections - Dicionários
- Tudo o que vimos em dicionários, vale para o Default Dict

Revisão de dicionários

dicionario = {'name': 'Gabriel', 'name2': 'Rafael'}
print(type(dicionario))
print(dicionario['name'])

dicionario = dict(name='Gabriel', name2='Rafael')
print(type(dicionario))

OBS: Lambdas são funções sem nome que podem ou não receberem parâmetros de entrada e retornar valores.

- Basicamente, a vantagem em utilizar esta lib é o fato de não gerar um KeyError
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)


dicionario['curso'] = 'Programação em Python do básico ao avançado'
print(dicionario)

# Em dicionário normal, tentar acessar uma chave que não existe gera um KeyError

print(dicionario['outro'], ' -> Gera isso e evita um KeyError')



