"""
* Conjuntos em Linguagem de Programação faz referência a Teoria dos Conjuntos da matemática
* São chamados de 'Sets' em Python
* Não possuem valores duplicados
* Não possuem valores ordenados
* Não são acessíveis por índice*

* São referenciados por chaves {}
- Diferença entre sets e dicionários:
    - Dicionários tem chaves e valores
    - Sets tem apenas valor
- Ele gera uma ordem própria de valores, diferente de lista, tupla e dicionários
"""
"""
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 3, 2, 1}) # Menos comum

print(s)
print(type(s))
# Não gera erro e ignora os números repetidos

# Mais comum

print()
print("Mais comum")
s = {1, 2, 3, 3, 2, 1}

print(s)
print(type(s))


# Para verificar se tem algum número no conjunto, utilziar o if

print()
conj = {1, 2, 3}

if 3 in conj:
    print('Tem o 3')
else:
    print('Não tem o 3')
"""
#################################################################
"""
Não tem como ordenar utilizando o sort()

ex: 
conj = {1, 3, 2, 1, 4, 5}
conj.sort()

print(conj)
"""

"""
Revisão de informações


dados = 3, 4, 4, 5, 99, 99, 12, 15, 15, 14
print()
print(f'Total de {len(dados)} elementos')
print()

# Aceitam valores duplicados
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')
print(type(lista))

# Aceitam valores duplicados
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print(type(tupla))

# Não aceitam chaves duplicadas
dicio = {}.fromkeys(dados, 'dados')
print(f'Dicionário: {dicio} com {len(dicio)} elementos')
print(type(dicio))

# Não aceitam valores duplicados
conj = set(dados)
print(f'Conjuntos: {conj} com {len(conj)} elementos')
print(type(conj))
"""
"""
cidades = ['Belo Horizonte', 'Cuiabá', 'São Paulo', 'Caxias do Sul', 'Belo Horizonte']
print('Cidades:', len(cidades))

# Quantas cidades únicas foram cadastradas? (Não se repetiram)
print(len(set(cidades))) # Tranformei em conjunto (Não recebe valores repetidos) e fiz a contagem
"""
#################################################################
"""
Adicionando elementos em conjuntos
- Lembrando que conjuntos são mutáveis
- Duplicidade não gera erro, é somente ignorado e não é adicionado
"""
adicionar = {1, 2, 3, 4}
print(adicionar)

adicionar.add(5)
print(adicionar)
#################################################################
"""
Removendo elementos
- Lembrando que conjuntos não são indexados (não tem índice)
- Se o valor não for encontrado, irá gerar um KeyError
"""
print()

"""
Forma 1
- Gera KeyErro
- Não retorna valores
"""

add = {1, 2, 3, 4, 5}
print(add)

viewValue = add.remove(5)
print(viewValue)
print(add)

print()

"""
Forma 2
- Não gera erros
- Também não retorna valores
"""

add = {1, 2, 3, 4, 5}
print(add)


viewValue = add.discard(5)
print(viewValue)

print(add)

"""
user = ' '
conj = set()

while user != "sair":
    user = input('Numeros...: ')
    conj.add(user)
if user == 'sair':
    conj.discard('sair')
print(conj)
"""
#################################################################
"""
Copiando conjuntos (Deep Copy e Shallow Copy)
- Lembrando: Usando .copy(), você cria outro caminho na memória com uma cópia dos valores
- Usando Shallow Copy você armazena os dados no mesmo espaço de memória que a variável copiada
"""
print()

# Forma 1 - Deep Copy
novoConjunto = add.copy()
novoConjunto.add(5)
print(novoConjunto)

# Forma 2 - Shallow Copy
novo = novoConjunto
print(novo)
#################################################################
"""
Removendo todos os valores do conjunto
"""
print()
conj = {1, 2, 3, 4, 5}

conj.clear()

print(conj)
#################################################################
"""
Utilizando métodos matemáticos dos conjuntos
- União de conjuntos
"""
# Union

estudantes_python = {'Marcos', 'Gabriel', 'Carlos', 'Gulherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Ana', 'Guilherme', 'Carlos'}

# Gerando um conjunto de estudantes com nomes únicos
# Forma 1 - Union

uniao = estudantes_java.union(estudantes_python)

print(uniao)

# Forma 2 - Utilizando o pipe (|)

uniao = estudantes_java | estudantes_python
print(uniao, 'Usando pipe')
#################################################################
"""
Intersecção de conjuntos
- Somente os estudantes que estudam em ambas as linguagens
"""
# Forma 1
print()
estudantes_python = {'Marcos', 'Gabriel', 'Carlos', 'Gulherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Ana', 'Guilherme', 'Carlos'}

intersecction = estudantes_python.intersection(estudantes_java)
print(intersecction)

# Forma 2

intersec = estudantes_python & estudantes_java

print(intersec, 'Utilizando "&"')
#################################################################
"""
Valores únicos do conjunto
"""
print()

so_python = estudantes_python.difference(estudantes_java)
print(so_python, 'Estudam somente Python')

so_java = estudantes_java.difference(estudantes_python)
print(so_java, 'Estudam somente Java')
#################################################################
"""
Maior, menor, soma e tamanho
"""
print()

numbers = {0, 1, 2, 3}

print('Valor máximo:', max(numbers))
print('Valor mínimo: ', min(numbers))
print('Soma de valores: ', sum(numbers))
print('Tamanho: ', len(numbers))
