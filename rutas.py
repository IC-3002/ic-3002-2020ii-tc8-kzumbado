def contar_rutas_mas_cortas(C):
    m= len(C)
    n= len(C[0])

    if C[0][0] == 1:
        return 0

    for i in range(m):
        if C[i][0] == 0:
            C[i][0] = 1
        else:
            C[i][0] = 0

    for j in range(1, n):
        if C[0][j] == 0:
            C[0][j] = 1
        else:
            C[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if C[i][j] != 1:
                C[i][j] = C[i - 1][j] + C[i][j - 1]
            else:
                C[i][j] = 0

    return C[m - 1][n - 1]
