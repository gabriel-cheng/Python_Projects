"""
---------------------------------------
ESTRUTURAS CONDICIONAIS IF, ELSE, ELIF
---------------------------------------
"""
"""
idade = 6

if idade < 18:
    print("Menor de idade.")
else:
    print("Maior de idade.")
"""

"""
--------------------------------------------------------
"""
#EXEMPLO 1 (IGUAIS com (if) (Não é legal))
"""
numb1 = input("Informe um número...: ")
numb2 = input("Informe outro número...: ")
print()

if numb1 > numb2:
    print("O número %s é maior que %s!"%(numb1, numb2))
if numb1 < numb2:
    print("O número %s é menor que %s!"%(numb1, numb2))
if numb1 == numb2:
    print("Ambos são iguais!")
"""
"""
--------------------------------------------------------
"""

"""
--------------------------------------------------------
"""
#EXEMPLO 2 (IGUAIS com (else) (Pode fazer))

"""
numb1 = input("Informe um número...: ")
numb2 = input("Informe outro número...: ")
print()

if numb1 > numb2:
    print("O número %s é maior que %s!"%(numb1, numb2))
if numb1 < numb2:
    print("O número %s é menor que %s!"%(numb1, numb2))
else:
    print("Ambos são iguais!")
"""
"""
--------------------------------------------------------
"""
#EXEMPLO 3 (IGUAIS com (elif) (Recomendado))

"""
numb1 = input("Informe um número...: ")
numb2 = input("Informe outro número...: ")
print()

if numb1 > numb2:
    print("O número %s é maior que %s!"%(numb1, numb2))
if numb1 < numb2:
    print("O número %s é menor que %s!"%(numb1, numb2))
elif numb1 == numb2:
    print("Ambos são iguais!")
"""
"""
--------------------------------------------------------
"""