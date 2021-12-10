"""
Definindo funções
- "Cria partes no código que realizam tarefas específicas"
- Pode ou não receber uma entrada de dados e retornar uma saída de dados
- São úteis para executar procedimentos similares por repetidas vezes
OBS: Caso tenha que fazer uma função que execute diversas tarefas, sempre tentar simplificar o máximo possível
- Toda função recebe um parêntese.
"""
"""
Utilizando funções integradas (que já vem dentro da linguagem). OBS: São chamadas de Built-in
- Algumas funções devem ser utilizadas com dados específicos, ex:
.append() - Usado em listas
len() - Usado em diversos

- DRY - Don't Repeat Yourself (Não repita seu código)
"""

"""
Definindo funções em Python

def nome_da_funcao(parametros de entrada):
    bloco de função
    
- nome_da_funcao deve ser sempre em caixa baixa
- Se for mais de uma palavra, devem ser separadas por "_" ex: nome_da_funcao (Forma chamada de snakecase) 
- Parâmetros de entrada são opcionais, quando haver mais de um, devem ser separados por " , "
- Bloco da função, também chamado de corpo da função.
    - Pode ter ou não um retorno da função
"""
# Definição 1


def diz_oi():
    print('Oi')


"""
OBS: Dentro de uma função podem ser utilizadas outras funções
- Esta função não tem recenbendo nenhum parâmetro de entrada
- Esta função não retorna nada.
"""
# Utilizando a função
diz_oi()


def planetas():
    print('Mercúrio')
    print('Vênus')
    print('Terra')
    print('Marte')
    print('Júpiter')
    print('Saturno')
    print('Urano')
    print('Netuno')


planetas()





