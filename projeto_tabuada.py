"""
Projeto Tabuada em Python
"""

"""
Tipos de Ranges

# Tipo 1
    for num in range(11):
        print(num)
        
# Tipo 2
    for num in range(4, 11): # Imprimir de 4 até 10
        print(num)
        
# Tipo 3
    for num in range(5, 50, 5): # Imprimir de 5 até 45 de cinco em cinco números (ordem crescente)
        print(num)
        
# Tipo 4
    for num in range(5, 50, -5): # Imprimir de 45 até 5 de cinco em cinco números(ordem decrescente)
        print(num)
"""

multi = int(input("Quero ver a tabuada do...: "))

for num in range(0, 11):
    final = multi * num
    print(f"{multi} x {num} = {final}")

"""
Fim do algoritmo
"""