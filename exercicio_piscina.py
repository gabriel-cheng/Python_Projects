"""
Autor: Gabriel H. S. de Carvalho

Data: 26.10.2020

Função: Receber dados de usuários que querem ter acesso a uma piscina pública
"""

idMaior = ("18")
idade1 = input("Informe a sua idade....: ")
print()
nome1 = input("Informe seu nome...: ")
print()
varTem = input("Você está acompanhado(a)...? (S/N): ")
print()

if idade1 < idMaior:
    print("Desculpe, %s. Você não pode entrar na piscina por ser menor de 18 anos."%(nome1))
else:
    print("Você pode entrar, %s. Divirta-se!"%(nome1))
if varTem == "sim":
    idade2 = input("Informe a idade do acompanhante...: ")
    print()
    nome2 = input("Informe o nome do acompanhante...: ")
    print()
if idade2 < idMaior:
    print("Desculpe, %s. Você é de menor, portanto não pode participar do evento!"%(nome2))
else:
    print("Bem-vindo ao evento, %s! divirta-se com seu(sua) amigo(a) %s."%(nome2, nome1))
