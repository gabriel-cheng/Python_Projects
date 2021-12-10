"""
Saindo de loop com break
"""
# Exemplo 1 de uso do Break
"""
for num in range(0, 7):
    if num == 6:
        break
    else:
        print(num)
print("Sai do loop!")
"""

# Exemplo 2 de uso do break
while True:
    sair = input("Digite 'sair' para sair: ")
    if sair == "sair":
        print("Você saiu!")
        break