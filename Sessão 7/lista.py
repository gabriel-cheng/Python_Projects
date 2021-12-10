"""
Listas em Python

Funcionam como vetores ou matrizes (Arrays)

- Podemos criar a lista e ir adicionando elementos;
    - O quantidade que pode ser adicionada está relacionada ao tamanho da memória RAM;

- Pode ser adicionado qualquer tipo de dado;

- Basicamente, lista é tudo o que contém " []
- Listas aceitam repetição
- Parar interpolar é precisa colocar um "f" antes das aspas, ex:
    world = "mundo"
    print(f"Olá {world}")
"""
"""

lista = [1, 2, 3, 6, 5, 4, 7, 9, 8, 10, 9, 15, 14, 13, 12, 11, 20, 20, 1, 2]


lista.sort() # Utilizando o DIR([])
print(lista)
print()
print(lista.count(20)) # Faz a contagem de quantos "20" há na lista
"""

###########################################################################

"""
Append
# Adicionando elementos numa lista utilizando a função "append"
"""
numbers = [1, 2, 3]

numbers.append(4) # Incremente o elemento como uma unidade à lista
print(f"{numbers} (utilizando append)")

###########################################################################
"""
Extend
# Adicionando elementos numa lista utilizando a função "extend"
# Não aceita valores únicos
"""
numbers.extend([5, 6, 7]) # Incrementa o elemento como um valor adicional à lista
print(f"{numbers} (utlizando extend)")

###########################################################################
"""
Insert
# Também podemos inserir um valor informando a posição
# Insert faz com que o índice informado e o valor sejam adicionados à lista
"""
numbers.insert(1, 'Novo valor') # Índice, valor
print(numbers)

##########################################################################
# Operação de adição com listas

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
inter = lista1 + lista2

print(inter, "Lista inter")
###########################################################################
# Inverter a ordem dentro de uma lista

lista1.reverse()
print(lista1, " - Utilizando reverse")

# Outra forma de inverter

lista = lista1[::-1] # Slicing (conteúdo de string)
print(lista, " - Utilizando [::-1]")
###########################################################################
# Copiar lista

copyLista = lista.copy()
print(copyLista, " - Utilizando copy")
###########################################################################
# Fazendo contagem de elementos dentro de uma lista

print("Contém", len(lista), "elementos")
###########################################################################
# Removendo o último elemento com pop

print(f"{lista} - Sem pop")
lista.pop()
print(f"{lista} - Com pop")

# Removendo elemento pelo índice

lista.append(4)
lista.pop(1)

print(f"{lista} - Removendo por índice")
###########################################################################
"""
lisTest = ['G', 'H']
resp = input("Deseja remover algum elemento? ")

if resp == "sim":
    resp2 = int(input("Informe o índice (0 = 'G'/1 = 'H'): "))
    if resp2 == 0:
        lisTest.pop(0)
        print(f"Índice removido! Lista atual: {lisTest}")
    elif resp2 == 1:
        lisTest.pop()
        print(f"Índice removido! Lista atual: {lisTest}")
    else:
        print("Informe um número válido!")
else:
    print("Obrigado por utilizar nossos serviços!")
"""
###########################################################################
# Removendo todos os elementos de uma lista

listaLimpa = [1, 2, 3, 4]
listaLimpa.clear()
print(listaLimpa, " -  Removendo elementos da lista")

# OBS: Se torna uma lista vazia
###########################################################################
# Podemos repetir os elementos da lista multiplicando-os, ex:

nova = [1, 2, 3]
print(nova, " - Elementos sem multiplicar")

nova = nova * 3
print(nova, " - Lista mutliplicada por 3")
###########################################################################
# Transformando string em lista

nome = 'Gabriel Carvalho'
nome = nome.split() # As palavras com espaço se tornam os elementos da lista

print(nome, " - Convertido em lista")

# Exemplo 2, definindo o padrão de listagem

nome2 = 'Gabriel,Carvalho,Souza'
nome2 = nome2.split(',')

print(nome2, ' - Utilizando vírgula como separador')
###########################################################################
lista = ['Gabriel', ' Carvalho', ' Souza']
nome = " ".join(lista) # Informei que converti uma string separando-as com espaços)

print(nome, ' - Convertendo lista em string')
# Posso escolher qualquer separador
###########################################################################
# Iterando sobre uma lista
listaNew = lista2
listaNew.sort()

for elemento in listaNew:
    print(elemento, ' - Iterando sobre lista')
###########################################################################
"""
carrinho = []
produto = " "

while produto != "sair":
    print("+Adicionar (digite 'sair' para sair): ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""
###########################################################################
# Numa lista, pode ser acessado de modo inverso informando o índice na casa do negativos, ex:
lista = [1, 2, 3, 4]
print(lista[-1])
###########################################################################

"""
cores = ['Verde', 'Azul', 'Amarelo', 'Preto']

for cor in cores:
    print(cor)

i = 0
while i < len(cores):
    print(cores[i])
    i = i + 1
"""
###########################################################################
"""
# Revisando o uso do enumerate
print()
print("Utilizando o enumerate")
print()

cores = ['Azul', 'Preto', 'Amarelo', 'Marrom']
for i, cor in enumerate(cores): # i = indice do elemento / cor = nome do elemento
    print(i, cor)

# Outra forma
cores = list(enumerate(cores))
print(cores, ' - Outra forma de utilizar enumerate')
"""
###########################################################################
# Verificar o índice por seu valor, ex:
# Se houverem dois valores com o mesmo índice, ele informará somente o valor do primeiro índice

cores = ['Azul', 'Marrom', 'Preto', 'Amarelo', 'Marrom', 'Verde']
print(cores.index('Marrom')) # Informar o primeiro "Marrom"

print(cores.index('Marrom', 2)) # Informa o índice do próximo valor 'Marrom' depois do índice 2

print(cores.index('Marrom', 3, 5)) # Imprime o índice do valor que está entre os índices "3" e "5"

"""
print(cores)
resp = input("Informe o nome da cor para saber o índice: ")
cor = list(cores)


# algoritmo que recebe o nome de uma cor informada pelo user e imprime seu índice
if resp:
    print("O índice da cor " + resp + " é: ", cores.index(resp))
"""
###########################################################################
# Revisão de slicing

# lista: [Inicio:fim:passo]
# Range: [Inicio:fim:passo]
###########################################################################
# Somando uma lista e imprimindo o maior e o menor valor
# Somente se todos os valores forem inteiros ou float

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista), " - Soma") # Soma todos os elementos
print(max(lista), " - Maior valor")
print(min(lista), " - Menor valor")
print(len(lista), " - Tamanho da lista")
###########################################################################
# Desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
###########################################################################
# Em python existem dois tipos de cópias, Shallow Copy e Deep Copy

# Deep Copy:
print()
print("Deep Copy")

lista = ['a', 'b', 'c']
print(lista, "- Lista")
novaLista = lista.copy()
print(novaLista, "- Nova lista")

novaLista.append('d')

print(lista, "- Primeira lista")
print(novaLista, "- Nova lista com letra 'd'")

# Shallow Copy
print("-------------------------------------")
print("Shallow Copy")

lista = ['a', 'b', 'c']
print(lista, '- Lista 1')

nova = lista
print(nova, '- Nova lista')
nova.append('d')

print(lista, '- Lista 1')
print(nova, '- Nova lista')

# Basicamente, a diferença é que:
#   - Deep copy: Copia o conteúdo da lista
#   - Shallow Copy: Copia o conteúdo da lista, mas direciona o mesmo caminho da memória pra ambas
