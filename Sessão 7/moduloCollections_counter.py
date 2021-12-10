"""
Módulo Collections - Counter
- Podemos utilizar QUALQUER iterável
- Ele gera praticamente um contador de elementos, por exemplo:
    lista = [1, 1, 2, 2]
    contar = Counter(lista)
    print(contar)

    Counter({1: 2, 2:2}) # "Número 1 há 2 elementos, número 2 há 2 elementos"


# Exemplo 1

from collections import Counter

lista = [1, 3, 4, 3, 1.22, 1.22, 1, 1.22, 1.33, 1.1, 11, 11, 12, 12.2]

resp = Counter(lista)
print(type(resp))
print(resp)

# Exemplo 2

from collections import Counter

print(Counter('Gabriel Carvalho'))
"""
from collections import Counter

texto = """Macunaíma, o herói sem nenhum caráter é um livro publicado em 1928 pelo polímata brasileiro Mário de Andrade, 
considerado a sua obra-prima. Escrito em pouco tempo mas fruto de pesquisas anteriores 
que o autor fazia sobre as origens e as 
especificidades da cultura e do povo brasileiro, narra a história do herói índio Macunaíma
desde seu nascimento na selva até sua morte e transfiguração, uma trajetória movimentada e aventuresca
em que é ajudado por seus irmãos e outros personagens, em busca de uma pedra mágica, o muiraquitã, 
que havia recebido de seu grande amor, Ci, a Mãe do Mato, mas que fora perdida e acabara em posse de Piaimã, 
um gigante comedor de gente que vivia como abastado burguês em São Paulo.
A obra é de difícil classificação no sistema dos gêneros literários, sua estrutura tem elementos
de muitos gêneros combinados, mas é muito elogiada como um experimento linguístico e literário extraordinariamente
original e bem-sucedido, que esconde sua erudição na aparente facilidade com que integra modos de falar e elementos 
de crônicas, lendas, ditados e contos folclóricos de todo o Brasil em uma narrativa 
coerente, vigorosa, ágil e cativante."""

lista = texto.split()
contar = Counter(lista)
print(contar)

# Função que mostra quais palavras são as que mais mostram

print(contar.most_common(5)) # As 5 que mais se repetem


