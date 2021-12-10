"""
--------------------------------------------------------------------------------------
TIPO STRING

Já vimos que em Python, um dado é considerado do tipo String sempre que:

- Estiver entre aspas simples ('string');
- Estiver entre aspas duplas ("string");
- Estiver entre aspas simples triplas ('''string''');

nome = '''Geek University'''
print(nome)
print(type(nome))

print()
print()

nome = "Gina's Bar"
print(nome)
print(type(nome))

print()
print()

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print()
print()

# [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10, 11,   12, 13,  14,  15]   
#['G', 'A', 'B', 'R', 'I', 'E', 'L', ' ', 'C', 'A', 'R', 'V', 'A', 'L', 'H', 'O'] 
nome = 'Gabriel Carvalho'
print(nome[0:7]) #_Slice de string

#[   0,           1,]
#['Gabriel', 'Carvalho']
print(nome.split()[1])

"""
#- Estiver entre aspas duplas triplas ("""string""");
"""
OBS: Qualquer coisa que estiver dentro de aspas é considerado String.
--------------------------------------------------------------------------------------
"""

nome = 'Gabriel Carvalho'
print(nome[::-1]) #Inversão da String
print()
print(nome.replace('G', 'P').replace('a', 'o'))
print(type(nome))

print()

texto = 'socorram me subino onibus em marrocos'
print(texto)
print()
print(texto[::-1])
print()
