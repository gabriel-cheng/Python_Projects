"""
Mapas em Python são chamados de dicionários
"""
meses = dict(jan='100', fev='250', mar='400')
print(meses)

# Iterar sobre dicionários
for chave in meses: # Imprime as chaves
    print(chave)

for chave in meses: # Imprime os valores
    print(meses[chave])

for chave in meses:
    print(f"Em {chave} recebi R${meses[chave]},00")

# Função para imprimir chaves
print(meses.keys()) # Isto irá imprimir as chaves do dicionário

"""
Forma correta em Python para acessar chaves
"""
print()
print("Forma correta de acessar chaves em Python:")
meses = dict(jan='100', fev='250', mar='400')

for chaves in meses.keys():
    print(chaves)

"""
Forma correta em Python de acessar valores
"""
print()
print("Forma correta de acessar valores em Python:")

print(meses.values())

for valores in meses.values():
    print(valores)

###############################################################
"""
Desempacotamento em dicionários
"""
print()
print("Desempacotamento de dicionários")
luas = dict(saturn='Ganimedes', jupiter='Galileanas', terra='Lua')
print(luas.items())

for chave, valor in luas.items():
    print(chave, '->', valor)
###############################################################
"""
Valor máximo, minimo e tamanho
* O comando 'sum' só deve ser utilizado em valores INT ou FLOAT
"""
print()
print("Valores máximo, mínimo e o tamanho")
satelites = dict(saturn='Ganimedes', jupiter='Galileanas', terra='Lua')

# print(max(satelites)) - Deve ser utilizado com INT e FLOAT
# print(min(satelites)) - Deve ser utilizado com INT e FLOAT
print(len(satelites))

