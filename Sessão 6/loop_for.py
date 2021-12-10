"""
Loop for

Exemplos de interáveis
- String
    nome = "Gabriel"
- Lista
    [1, 2, 3, 4, 5]
- Range
    numeros = range[1, 10]
- Iterar é o mesmo que imprimir 1 elemento de cada, ex:
    varTeste = 'Gabriel Carvalho'
    - Iterar no caso seria imprimir cada letra do nome separadamente

"""

"""
Para interpolar é preciso colocar um "f", ex:
    print(f"Interpolar {isto}")

nome = "Gabriel Carvalho"
numero = range(1, 10)
lista = [1, 3, 5, 7, 9]

#Exemplo de for iterando sobre uma string
for letra in nome:
    print(letra)

#Exemplo de for iterando sobre lista
for numero in lista:
    print(numero)

#Exemplo de for iterando sobre um range
for numero in range[1, 10]:
    print(numero)
    
O RANGE nunca vai imprimir o último valor, a menos que seja informado manualmente, ex:
    range(1, 10) -> Não vai imprimir até 10;
    range(1, 10) -> Vai imprimmir até 10;

"""
nome = 'Gabriel Carvalho'

for letra in enumerate(nome): # "Enumerate" é uma função que enumera toda a string
    print(letra)

print("*///////////////////////////////////////*")

for indice, letra in enumerate(nome): # Imprime todas as letras em formato crescente
    print(nome[indice])

print("*///////////////////////////////////////*")

for indice, letra in enumerate(nome): # Imprime a string em relação a quantidade de letras contidas na variavel string
    print(nome)

print("*///////////////////////////////////////*")

for _, letra in enumerate(nome): # " _ " descarta um valor, no caso o "indice"
    print(nome)

print("*///////////////////////////////////////*")
"""
quantidade = int(input("Informe quantas vezes repetir: ")) # Utilizar este formato para imprimir uma quantidade
soma = 0

for n in range(1, quantidade):
    num = int(input(f"Informe um valor {n}/{quantidade}: "))
    soma = soma + num

print(f"A soma é {soma}")

print("*///////////////////////////////////////*")

nome = "Gabriel Carvalho"

for letra in nome:
    print(letra, end=" ") # Vai imprimir sem pular linhas

print("*///////////////////////////////////////*")
"""

# emoji = U0001F606 -> código unicode de um emoji
# link tabela unicode de emoji -> http://www.unicode.org/emoji/charts/full-emoji-list.html
# OBS: Barra inversa (\) é um caractere de escape (ignora o conteúdo seguinte)

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F606' * num)
