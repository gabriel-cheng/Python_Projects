"""
Funções com retorno
- Quando uma função retorna nenhum valor, o retorno é None
OBS: Quando você retorna um valor, é preciso imprimí-lo

OBS: Sobre o return:
    1 - Ela finaliza a função
    2 - Um uma função pode-se ter vários tipos de return
    3 - Podemos usar o return com qualquer tipo de dados, incluindo múltiplos valores
"""
"""
-> Exemplo de função sem retorno

def quadrado(): # Vai gerar um None
    print(7 * 7)
    
-> Definindo funçaõ com retorno
    -> Funções que deve retornar algum valor deve utilizar a palavra 'return'

def quadrado():
    return 7 * 7

retorno = quadrado()
print(quadrado)
    
- OBS: Não é necessário criar uma variável para retornar um valor.
"""
# Formas de utilizar o return
"""
# Forma 1
def quadrado():
    return 7 * 7

ret = quadrado()
print(f'Retorno: {ret}')

# Forma 2
def quadrado():
    return 7*7

print(f'Retorno 2: {quadrado()}')
"""
"""
Isto irá gerar um erro:

def numero():
    return 5 + 5 # A função é finalizada à partir do return
    print('olá') # Qualquer coisa que seja posta depois do return gerará um erro
"""
# Utilizando mais de um return
"""

def variavel():
    var = False
    if var:
        return 4
    elif var == None:
        return 5
    return 'Não'

print(variavel())
"""
# Em uma função podemos retornar qualquer tipo de dado
"""
def lista():
    return [1, 2, 3, 4]

print(lista())
"""
"""
- É uma forma pseudo-randômica por repetir valores, seria totalmente randômica se não houvessem repetições
- Gera valores pseudo-randômicos por valores entre 0 e 1
from random import random

def cara_coroa():
    jogo = random()
    if jogo > 0.5:
        return 'Cara'
    return 'Coroa'

print(cara_coroa())
"""
# O que gera o retorno de um random?
"""
from random import random


def retorno():
    retorno = random()
    return retorno

print(retorno())
"""





