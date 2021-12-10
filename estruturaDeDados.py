"""
TESTANDO ESTRUTURA DE DADOS EM PYTHON
"""
# Revendo algumas funções

vetor = [1, 2, 3, 3, 3,4, 5]
print(vetor)

vetor.extend([6, 7, 8])
print(vetor)

vetor[len(vetor):] = ["a", "b"]
print(vetor)

vetor.append(5)
print(vetor)

vetor.insert(len(vetor), "teste")
print(vetor)

vetor.remove(3)
print(vetor)

vetor.pop(0) # Pode ser removido por índice, retorna o valor do índice removido
print(vetor)

"""vetor.clear()
print(vetor)"""

# retorno = vetor.index(3, 3, 3)
# print(retorno, "aqui")

vetor.insert(3, 3)
print(vetor)

print("Aqui ->", vetor.index(3, 3, 4)) # Valor, início[procurar índice à partir de qual índice?], fim[procurar valor até que índice?]


print(f"Possui {vetor.count(2)} valore(s)")

vetor.reverse()
print(vetor)


from collections import deque

nomes = deque(["Gabriel", "Rafael", "Paulo"])
print("\n", nomes)

nomes.append("Rose")

print(nomes)

nomes.insert(0, "Sandro")
print(nomes)

nomes.popleft()
print(nomes)

quad = []

for x in range(10):
    quad.append(x**2)

print(quad)

quad2 = [x**2 for x in range(10)]
print(quad2)






