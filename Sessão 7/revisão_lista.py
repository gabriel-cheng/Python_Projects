"""
Revisão de listas
"""
#############################################################
"""
Listas base
"""

lista = [1, 2, 4, 3, 5, 6, 7, 9, 8, 10, 50, 32, 17]
listaNova = [1, 2, 3]
#############################################################
"""
Organização de lista em ordem crescente (sort())
"""

lista = [1, 2, 4, 3, 5, 6, 7, 9, 8, 10, 50, 32, 17]
print(lista)

lista.sort()
print(lista)

# Fazer a contagem de quantos números há repetidos na lista

lista2 = lista + [32, 1, 2, 3, 32, 32, 32]
print(lista2)

print(lista2.count(32))
#############################################################
"""
Organização de lista em ordem decrescente (reverse())
"""

listaDecre = [1, 2, 3, 4]
print(listaDecre)

listaDecre.reverse()
print(listaDecre, '- Reverse')
#############################################################
"""
Outra forma de inverter uma lista utilizando (Slicing[::])
"""
listaDecre = [1, 2, 3, 4]
print(listaDecre)

listaDecre = listaDecre[::-1] # [Inicio:fim:passo]
print(listaDecre, '- Slicing')
#############################################################
"""
Adicionando elementos únicos em uma lista (append())
- Só aceita uma unidade por vez
"""
listaNova = [1, 2, 3]
print(listaNova)

listaNova.append(4)
print(listaNova)
#############################################################
"""
Adicionando mais de um elemento em uma lista (extend())
- Não aceita elementos únicos
- OBS: É preciso adicionar os valores dentro de chaves
"""

listaNova = [1, 2, 3]
print(listaNova)

listaNova.extend([4, 5, 6, 7])
print(listaNova)
#############################################################
"""
Adicionando valores escolhendo a posição (insert())
"""

lista = [1, 2, 3, 4]
print(lista)

lista.insert(1, 2) # Indice, valor
print(lista)
#############################################################
"""
Operação de adição com listas
"""

listaAdicao = lista + listaNova
listaAdicao.sort()

print(listaAdicao)
#############################################################
"""
Cópia de lista dos tipos Deep Copy & Shallow Copy (copy())
Deep Copy
"""
lista = [1, 2, 3, 4, 5]
print(lista, '- Lista')

novaLista = lista.copy()
print(novaLista, '- Cópia')

"""
Shallow Copy
"""
lista = [1, 2, 3, 4, 5]
print(lista, '- Shallow Copy')

novaLista = lista
novaLista.extend(['Novo valor', 7, 8])
print(novaLista, '- novaLista Shallow Copy')
print(lista, '- Lista 1 Shallow Copy')
#############################################################
"""
Contagem de elementos dentro da lista (len())
"""
lista = [1, 2, 3]
print(f"A lista possui", len(lista), 'elementos')
#############################################################
"""
Removendo elementos com a função (pop())
"""
# Removendo o último elemento
lista = [1, 2, 3, 4]
print(lista)

lista.pop()
print(lista)

# Removendo por índice
lista = [1, 2, 3, 4]
print(lista)

lista.pop(2) # Removendo o valor 3 que está no índice 2
print(lista)
#############################################################
"""
Removendo todos os elementos de uma lista (clear())
"""
lista = [1, 2, 3, 4]
print(lista)

lista.clear()
print(lista)
#############################################################
"""
Multiplicando elementos
"""
lista = [1, 2, 3, 4]
print(lista)

lista = lista * 3
print(lista)
#############################################################
"""
Transformando string em lista com (split())
"""
nome = 'Gabriel Carvalho'

nome = nome.split(' ') # Dentro do parêntede defini-se o padrão de separação para listagem
print(nome)

# Exemplo 2
nome = 'Gabriel Carvalho'

nome = nome.split('a')
print(nome)
#############################################################
"""
Convertendo lista em string (join())
"""
nome = ['Gabriel', 'Carvalho']
string = ' '.join(nome) # Informei que a string utilizará o espaço como separador dos elementos
print(string)
#############################################################
"""
Iterando sobre lista (Loop for)
"""
lista = [1, 2, 3, 4, 5]

for numbers in lista:
    print(f'-> {numbers}')
#############################################################
"""
Acessando casas de modo inverso com slicing
"""
lista = [1, 2, 3, 4]
print(lista[-1])
#############################################################
"""
Revisando a função (enumerate())
"""
lista = [10, 20, 30, 40]

for numb in enumerate(lista): # Basicamente mostra os índices de uma lista
    print(numb)
#############################################################
"""
Verificando o índice do elemento pelo seu valor (index())
"""
# Se houverem dois valores iguais, ele informará somente o índice do primeiro
lista = ['Gabriel', 'Henrique', 'Souza', 'de', 'Carvalho']

print(f'Índice', lista.index('de'))

lista = [1, 2, 3, 4, 5, 5, 6, 5]
for numbers in enumerate(lista):
    print(numbers)
print (lista.index(5, 5)) # Visualizando um número repetido
#############################################################
"""
Informando valor máximo e mínimo, tamanho da lista e soma dos valores
"""
lista = [1, 2, 3, 4, 5, 6]

print('Soma dos elementos:', sum(lista)) # Soma dos elementos
print('Valor máximo:', max(lista)) # Maior valor
print('Menor valor:', min(lista)) # Menor valor
print('Tamanho:', len(lista)) # tamanho da lista
#############################################################
"""
Despacotamento de lista
"""
lista = [1, 2, 3, 4]

num1, num2, num3, num4 = lista

print(num1)
print(num2)
print(num3)
print(num4)


