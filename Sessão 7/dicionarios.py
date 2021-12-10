"""
Dicionários

- Em algumas linguagens de programação, dicionários em Python são conhecidos como Mapas
- É um mapeamento do chave/valor
- São representados por chaves {}
- dicionario = {'chave': 'valor, 'chave': 'valor'}
- Tanto a chave quanto o valor podem ser de qualquer tipo
- Podemos utilizar qualquer tipo de dado (int, str, float, bool, dict, tuplas, listas, etc.)
"""
"""
Forma 1 - mais comum
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

"""
Forma 2 - menos comum
"""
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

##########################################################################
"""
Acessando elementos
Forma 1
"""

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises['py'])
# print(paises['ru']) # Vai gerar um erro


"""
Forma 2 - Recomendado (Utilizando get)
"""
print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('py')
pais = paises.get('py', 'Sei lá')

if pais:
    print(f'Encontrei o {pais}')
else:
    print(f'Não encontrei o {pais}')
##########################################################################
"""
Verificando se o elemento está dentro da lista
"""
nomes = dict(
    ga='Gabriel',
    he='Henrique',
    so='Souza'
)

print('ga' in nomes) # É possível verificar somente a chave com este método

if 'ca' in nomes:
    Carvalho = nomes['ca']
##########################################################################
"""
Adicionando elementos em dicionários
- Não podemos ter chaves repetidas
- Caso você adicionar uma chave repetida, será alterado o valor daquela chave, e não adicionado
"""
# Forma 1 - Mais comum
nomes = dict(
    ga='Gabriel',
    he='Henrique',
    so='Souza'
)

print(nomes)

nomes['ca'] = 'Carvalho'

print(nomes)

# Forma 2
novo_nome = {'si': 'Silva'}
print(nomes)

nomes.update(novo_nome) # nomes.update({'si': 'Silva']})   <- Também pode ser utilizado
print(nomes)

# Atualizando conteúdo

nomes['ga'] = 'Rafael'
print(nomes)

nomes.update({'he': 'Antônio'})
print(nomes)

##########################################################################
"""
Deletando elementos
"""
# Forma 1
# Neste caso, o valor é retornado.
nomes = dict(ga='Gabriel', he='Henrique', so='Souza', ca='Carvalho')
print(nomes)

nomes.pop('so')
print(nomes)

# Forma 2 - Forma mais comum
# Neste caso, o valor não é retornado.
del nomes['ca']
print(nomes)
print('##########################################################################')
"""
Site de e-commerce com lista

produtos = ['Playstation 5', 'Refrigerante', 'Macarrão']
print(produtos)

print()

print('Para sair sair digite "sair"')
print('Para limpar o carrinho digite "limpar carrinho"')

print()

carrinho = []
cliente = ' '

while cliente != 'sair':
    cliente = input('+Adicionar ao carrinho...: ')
    carrinho.append(cliente)
    if cliente == 'sair':
        carrinho.pop()
        print(carrinho)
    elif cliente == 'clear' or cliente == 'limpar':
        carrinho.clear()
        print(carrinho)
for i, p in enumerate(carrinho):
    print(i, p)
"""
##########################################################################
"""
Site de e-commerce com Tuplas
- A tupla como sendo imutável, não se pode adicionar elementos usando append()
- O tipo do carrinho será sempre como lista, os produtos podem ser tuplas.


produtos = ('Playstation 5', 'Refrigerante', 'Macarrão')
print(produtos)

print()

print('Para sair sair digite "sair"')
print('Para limpar o carrinho digite "limpar carrinho"')

print()

carrinho = []
cliente = ' '

while cliente != 'sair':
    cliente = input('+Adicionar ao carrinho...: ')
    carrinho.append(cliente)
    if cliente == 'sair':
        carrinho.pop()
        print(carrinho)
    elif cliente == 'clear' or cliente == 'limpar':
        carrinho.clear()
        print(carrinho)
for i, p in enumerate(carrinho):
    print(i, p)
print(type(produtos))
"""
##########################################################################
"""
Sistema de e-commerce com dicionários


produtos = dict(ps4='Playstation 4', refri='Refrigerante', uva='Uva')
print(produtos)

carrinho = dict()
cliente = ' '

while cliente != 'sair':
    cliente = input('+Adicionar ao carrinho...: ')
    carrinho.append(cliente)
    if cliente == 'sair':
        carrinho.pop()
print(carrinho)
"""
##########################################################################
"""
Limpando um dicionários utilizando clear()
"""
d = dict(a=1, b=2, c=3)
print(d)

d.clear()
print(d)
##########################################################################
"""
Copiando dicionários com copy() - Deep Copy
"""
d = dict(a=1, b=2, c=3)
print(d, 'Dict d')

novo = d.copy()

print(novo, 'Dict novo')
novo['d'] = 4
print(novo, 'Dict novo+4')

"""
Shallow Copy
"""
novo = d
print(novo, 'Shallow Copy')
##########################################################################
"""
Método não usual de criação de dicionários
"""

outro = {}.fromkeys('a', 'b') # 'a' é a chave e 'b' é o valor

print(outro)
print(type(outro))

# Outra forma

outro = {}.fromkeys(['nome', 'email', 'sexo'], 'desconhecido')
# Todas as strings dentro da crave são chaves de 'desconhecido'

print(outro)
print(type(outro))

# Outra forma

outro = {}.fromkeys('chave', 'valor')
# Cada letra da palavra 'chave' se tornou uma chave com valores iguais a 'valor'
# Lembrando: em dicionários Python, não há repetição de chaves.
print(outro)

# Outra forma

usingRange = {}.fromkeys(range(1, 11), 'valor')
print(usingRange)
##########################################################################





