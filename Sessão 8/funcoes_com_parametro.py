"""
Funções com parâmetros

- Funções que recebem dados e processam dentro da mesma;

Pensando em qualquer computador comum temos:

Entrada -> Processamento de dados -> Saída

Tipos de funções que sabemos
- Não possuem entrada
- Não possuem saída
- Possuem entrada mas não possuem saída
- Possuem saída não possuem entrada
- Possuem entrada e saída
"""

# Refatorando uma função


def calc(numero):
    return numero * numero


print(calc(2))
print(calc(10))
print(calc(8))


"""
Podem ser declarados quantos parâmetros forem necessários
- A ordem de entradas será na sequência informada 
"""
# Exemplos de funções com parêmetros


def calcula(a, b):
    return a + b


def multiply(a, b):
    return a * b


def outro(num, b,  msg):
    return num + b * msg


print(calcula(3, 6))
print(calcula(4, 2))
print(calcula(3, 2))







