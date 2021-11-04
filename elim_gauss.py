matriz = [[3, 2, 4, 1], [1, 1, 2, 2], [4, 3, -2, 3]]

for i in range(0, len(matriz)):
    pivo = matriz[i][i]
    a = i+1
    for j in range(a, len(matriz)):
        matriz[j][a] = matriz[j][a] / pivo
        m = matriz[j][a]
        for k in range(0,len(matriz[0])):
            matriz[j][k] = matriz[j][k] - m * matriz[i][k]
    print(matriz)


