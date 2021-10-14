def bfs(g, no_ini):
    """
    Executa o algoritmo BFS (breadth fist search) no grafo "g" a partir de um nó inicial "no_ini"
    :param g:
    :param no_ini:
    :return:
    """
    n = len(g)
    visitados = [False] * n
    q = [] # a queue será uma lista
    q.append(no_ini)
    while (q):
        x = q.pop(0)
        if not visitados[x]:
            print(x)
            visitados[x] = True
            for y in range(n):
                if (g[x][y] == 1) and (not visitados[y]):
                    q.append(y)

grafo = [
    [0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0]
]

bfs(grafo,0)