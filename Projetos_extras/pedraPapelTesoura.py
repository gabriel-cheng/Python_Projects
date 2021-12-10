"""
Pedra, Papel e Tesoura
"""

from random import random


def jogar(jogada):
    jogada = range(1, 3)
    if (jogada == 1):
        return "Pedra"
    elif (jogada == 2):
        return "Papel"
    else:
        return "Tesoura"


jogar()
