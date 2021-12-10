"""
Tuplas

Diferenças:
    - São compostas por parênteses
    - Tão são imutáveis, como as contantes, não podem ser alteradas.

- São considerado tuplas:
    - tupla1 = (1, 2)
    - tupla2 = 1, 2
    - tupla3 = 1,
"""
"""
Tipos de tuplas
"""
tupla1 = ('Gabriel', 'Carvalho', 2, 3, 'Souza')
print(tupla1)
print(type(tupla1))

"""
Isto também é considera um tupla
"""
tupla2 = 'Gabriel', 2, 'Carvalho', 4, 'Souza'
print(tupla2)

"""
Tuplas são definidas pela vírgula, não pelo uso do parêntese
"""
tupla3 = (4) # Não é uma tupla, mas é lido formato int
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))
###########################################################################
"""
Tuplas com range
"""

tupla = tuple(range(10))
print(tupla)
print(type(tupla)) # Podemos gerar um tupla usando range(inicio, fim, passo)
###########################################################################
"""
Desempacotamento de tupla
"""
nome = 'Gabriel', 'Carvalho'
print(type(nome))

string1, string2 = nome
print(string1, ' (Desempacotamento)')
print(string2, ' (Desempacotamento)')
###########################################################################
"""
Soma de tuplas
"""
numbers = 1, 2, 3
numbers2 = 4, 5, 6

numberSoma = numbers + numbers2

print(type(numberSoma))
print(numberSoma)
###########################################################################
"""
Valores máximos, mínimos, tamanho da tupla
"""
numbers = 1, 2, 3, 4

print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(len(numbers))
###########################################################################
"""
Concatenação de tuplas
"""
tuple1 = 1, 2, 3, 4, 5
tuple2 = 6, 7, 8, 9, 10

print(tuple1 + tuple2) # Isso concatena, não soma
###########################################################################
"""
Verificando valores na tupla
"""

tupla = 1, 2, 3, 4, 5, 'Novo valor'

print(4 in tupla)
###########################################################################
"""
Iterando sobre tuplas
"""
tupla = 1, 2, 3

for num in tupla:
    print(num)

for indice, valor in enumerate(tupla):
    print(indice, valor)

###########################################################################
"""
Contando elementos em tuplas
"""
tupla = 1, 2, 3, 4, 5, 5, 4, 3, 2, 1

print(tupla.count(4))
###########################################################################
"""
Convertendo string em tuplas
"""
nome = tuple('Gabriel Carvalho')

print(type(nome))
print(nome)
###########################################################################
# Basicamente, tudo o que você faz em lista, você pode fazer em tuplas.




