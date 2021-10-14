"""
Criado em 05/10/2021 para a aula de Programação Avançada

@author: Francisco Rubens
"""

def bfs(g, rotulos, rotulo_inicial):
    """
    Algorirmo BFS
    :param g:
    :param rotulos:
    :param inicial:
    :return:
    """
    n = len(g)
    no_ini = rotulos.index(rotulo_inicial)
    visitados = [False] * n
    q = [] # a queue será uma lista
    q.append(no_ini)
    hops = [0] * n # lista de hops (número de arestas da origem ao nó)
    caminho = [] # resultado retornado pela função
    while (q):
        x = q.pop(0)
        if not visitados[x]:
            caminho.append(x)
            visitados[x] = True
            for y in range(n):
                if (g[x][y] == 1) and (not visitados[y]):
                    q.append(y)
                    if hops[y] == 0:
                        hops[y] = hops[x] + 1

    return [[rotulos[i], hops[i]] for i in caminho]

rotulos = ['Frank', 'Rakesh', 'Eiben', 'Kamber', 'Han']

grafo = [
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,0]
]

rotulo_no_inicial = 'Han'
resultado = bfs(grafo, rotulos, rotulo_no_inicial)
print('BFS do nó', rotulo_no_inicial + ':')
print(resultado)