"""
AUTOR: Gabriel H. S. de Carvalho

DATA: 26/10/2020

FUNÇÃO: Dar início ao primeiro script feito em Python utilizando
estrutura de condição
"""

#Inicio
numb1 = input("Informe o primeiro número...: ")
numb2 = input("Informe um segundo número...: ")
print()

if numb1 > numb2:
    print("O número %s é maior que %s!"%(numb1, numb2))
if numb1 < numb2:
    print("O número %s é menor que %s!"%(numb1, numb2))
elif numb1 == numb2:
    print("Ambos são iguais!")
#fimalgoritmo
