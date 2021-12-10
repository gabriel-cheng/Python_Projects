"""
Módulo Collections - Deque

- Podemos dizer que Deque é uma lista de alta performance
- Você consegue manipular tanto o final quando o início (inserção ou remoção)
"""
from collections import deque

deq = deque('Gabriel') # Ele gera uma lista com todas as letras da string
print(deq)
print(type(deque))

"""
# É o mesmo que
nome = 'G,a,b,r,i,e,l'

nome = nome.split(',')
print(nome)
print(type(nome))
"""

"""Adicionando elementos na no Deque"""

deq = deque('Gabriel')

deq.extend([' ', 'C'])

deq.append('.')
print(deq)

deq.appendleft('->') # Adiciona no começo da lista
print(deq)

"""Removendo elementos"""
deq = deque('Gabriel')
print(deq)

deq.pop() # Remove e retorna o valor
print(deq)

deq.popleft() # Remove o primeiro valor
print(deq)
