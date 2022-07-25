def cria_mat(qtde_linhas, qtde_colunas, valor=0):
    m = qtde_linhas * [0]
    for i in range(qtde_linhas):
        m[i] = qtde_colunas * [valor]
    return m


def multiplica_matriz(ma, mb):
    linhas_mr =  len(ma)
    colunas_mr = len(mb[0])
    mr = cria_mat(linhas_mr, colunas_mr)
    for i in range(linhas_mr):
        for j in range(colunas_mr):
            for k in range(len(mb)):
                mr[i][j] = mr[i][j] + ma[i][k] * mb[k][j]
    return mr
