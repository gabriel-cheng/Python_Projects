"""
Módulo Collections - Named Tuple
"""
from collections import namedtuple
"""
from collections import namedtuple

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')
# É como se fosse 3 variáveis para o 'cachorro': idade, raça e nome

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Forma mais clara
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

- Basicamente, facilita na forma de fazer acesso aos elementos da tupla
"""
humano = namedtuple('humano', ['nome', 'idade', 'sexo'])

ray = humano(nome='Gabriel', idade=23, sexo='Masculino')

"""
Formas de acessar elementos
"""
# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])
print()

# Forma 2
print(ray.nome)
print(ray.idade)
print(ray.sexo)
print()

# Forma 3
print(ray.index('Gabriel'))
print(ray.index(23))
print(ray.index('Masculino'))
