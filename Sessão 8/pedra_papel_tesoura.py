"""
Jogo - Pedra, Papel e tesoura
"""
import random


def joga():

    jogada = random.randrange(10) # Gera e retorna um número de 0 a 10, basicamente igual a função range.

    if jogada <= 3: # De 0 a 3
        return 'Pedra'
    elif jogada <= 6: # 3 a 6
        return 'Papel'
    else: # 6 a 9
        return 'Tesoura'


print()
print(joga()) # Deve-se utilizar a funnção print sempre que gerar ou pedir-mos retorno.
