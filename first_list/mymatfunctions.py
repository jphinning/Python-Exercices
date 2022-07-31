
import copy 

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

def multiplica_matriz_escalar(escalar, m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] *= escalar 
    
    return m

def maior_matriz(m):
    maior_valor = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(maior_valor < m[i][j]):
                maior_valor = m[i][j]

    return maior_valor

def menor_matriz(m):
    menor_valor = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(menor_valor > m[i][j]):
                menor_valor = m[i][j]

    return menor_valor

def matriz_soma(m):
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma += m[i][j]  

    return soma

def regra_Sarrus(m):
    det_soma = 0
    det_subtracao = 0
    for i in range(3):
        det_soma += m[0][i] * m[1][(i + 1) % 3] * m[2][(i + 2) % 3]
        det_subtracao += m[2][i] * m[1][(i + 1) % 3] * m[0][(i + 2) % 3]

    return det_soma - det_subtracao

def acha_cofactor(lin, col, matriz):
    m_cofator = copy.deepcopy(matriz)
    print(matriz)
    #Elimina col da matriz 
    for i in range(len(m_cofator)):
        for j in range(len(m_cofator[i])):
            if (j == col):
                del(m_cofator[i][j])
    
    #Elimina linha
    del(m_cofator[lin])
    
    det_cofator = regra_Sarrus(m_cofator)

    return (-1)**(lin + col) * det_cofator


def regra_Laplace(m):
    # Determinante eh uma soma de cofator * elemento
    det = 0
    for j in range(len(m[0])):
        det += m[0][j] * acha_cofactor(0, j, m)

    return det

def retorna_transposta(m):
    mt = copy.deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            mt[i][j] = m[j][i]

    return mt