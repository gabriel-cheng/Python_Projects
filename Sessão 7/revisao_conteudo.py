"""
Revisão de conteúdo 2
"""
# Modulo collections - Counter

"""
from collections import Counter

texto = "Olá, meu nome é Gabriel, eu tenho 23 anos de idade e estou estudando de Análise e Desenvolvimento," \
        "de Sistemas. Moro em Araçatuba, mas sou nato de Andradina, o que por sinal é uma cidade," \
        "que fica logo ao lado."

contador = Counter(texto)
print(contador.most_common(2))

user = ' '
lista = []

while user != 'sair':
    user = input('Insira um número na lista...: ')
    lista.append(user)
    if user == 'sair':
        lista.pop()
        user = input('Deseja ver os dois mais repetidos...(S/N)? ')
        if user == 'sim':
            contar = Counter(lista)
            print(contar.most_common(2))
        else:
            break
print(lista)
"""
