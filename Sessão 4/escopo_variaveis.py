"""
-------------------------------------------------------------------------------------------------
ESCOPO DE VARIÁVEIS

Dois casos de escopo:

1- Variáveis globais;
    - São reconhecidas, ou seja, seu escopo compreende todo o programa.

2- Variáveis locais;
    - São reconhecidas apenas no bloco onde for declaradas, ou seja, seu escopo está limitado
    ao bloco onde foi declarada;

Para declarar variáveis em Python, fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica

> Uma variável global é quando ela pode ser utilizada em qualquer parte do código;
> Uma variável local é quando ela pode ser utilizada somente dentro de uma parte específica no código;
-------------------------------------------------------------------------------------------------
"""
"""
numero = 42.5 #Exemplo de variável global
print(numero)
print(type(numero))
print()
numero = 45
print(numero)
print(type(numero))
print()
numero = 'Gabriel'
print(numero)
print(type(numero))
print()
numero = '45'
print(numero)
print(type(numero))
"""

numb = 30#Variavel global

if numb > 10:
    novo = numb + 10 #Variavel local
    print(novo)
