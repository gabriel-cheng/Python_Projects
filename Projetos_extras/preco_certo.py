"""
Projeto Preço certo
"""

from random import randrange

geradorAleatorio = randrange(1, 30) # Gera um número pseudoaleatório de 1 ~ 6
print(geradorAleatorio)

count = 20

print("===Regras do jogo===")
print("-> Enquanto sua pontuação for maior que 10, você perderá 2 pontos por erro.")
print("-> Se sua pontuação for à partir de 10, você perderá 4 pontos por erro.")
print("\n", f"-> Sua pontuação atual: {count}\n")

while (count >= 1):
    count = count - 2
    user = int(input("Chute um valor entre 1 e 6...: "))
    if (user == geradorAleatorio):
        print(f"Correto! Sua pontuação foi de {count} pontos.\n")
        break
    else:
        print(f"Incorreto! Sua pontuação atual é {count}\n")
        if (geradorAleatorio > user):
            print(f"Dica: O número correto é maior que {user}\n")
        else:
            print(f"Dica: O número correto é menor que {user}\n")
    if (count < 2):
        print("Suas tentativas se esgotaram!")
        break


