import numpy as np

from mymatfunctions import *
from mymatutils import *

def multiplicacao_matrizes():
    m, n = ler_dimensao("Matriz A") # desempacotou a tupla, respectivamente em uma dupla atribuição
    o, p = ler_dimensao("Matriz B")
    if n == o: # verificar se pode multiplicar
        # criação das matrizes
        ma = cria_mat(m, n)
        ler_matriz("Matriz A", ma)
        mb = cria_mat(o, p)
        ler_matriz("Matriz B", mb)

        mres = multiplica_matriz(ma, mb)
        mres_numpy = np.matrix(ma) @ np.matrix(mb)
        imprime_mat("Matriz A", ma)
        imprime_mat("Matriz B", mb)
        imprime_mat("Matriz R = A * B", mres)
        imprime_mat("Matriz R Numpy = A * B", mres_numpy)
    else:
        print(f"Coluna de A {n} é diferente da linha de B {o}. Não posso multiplicar!")

def multiplicar_matriz_por_escalar():
    escalar = ler_escalar()
    m, n = ler_dimensao("Matriz")
    ma = cria_mat(m, n)
    ler_matriz("Matriz", ma)
    mr = multiplica_matriz_escalar(escalar, ma)
    imprime_mat("Matriz Resultante", mr)

def maior_menor_soma():
    m, n = ler_dimensao("Matriz")
    ma = cria_mat(m, n)
    ler_matriz("Matriz", ma)
    soma = matriz_soma(ma)
    maior_valor = maior_matriz(ma)
    menor_valor = menor_matriz(ma)
    imprime_mat("Matriz ", ma)
    print(f'Soma: {soma} \nMaior Valor: {maior_valor} \nMenor Valor: {menor_valor} ')
    print(f'Métodos Numpy\nSoma: {np.matrix.sum(np.matrix(ma))} \nMaior Valor: {np.matrix.max(np.matrix(ma))} \nMenor Valor: {np.matrix.min(np.matrix(ma))} ')

def det_Sarrus():
    ma = cria_mat(3, 3)
    ler_matriz("Matriz 3x3", ma)
    det = regra_Sarrus(ma)
    imprime_mat("Matriz ", ma)
    print(f'Determinante: {det} \n')
    print(f'Determinante Numpy: {np.linalg.det(np.matrix(ma))} \n')

def det_Laplace():
    ma = cria_mat(4, 4)
    ler_matriz("Matriz 4x4", ma)
    det = regra_Laplace(ma)
    imprime_mat("Matriz ", ma)
    print(f'Determinante: {det} \n')
    print(f'Determinante Numpy: {np.linalg.det(np.matrix(ma))} \n')

def transposta():
    m, n = ler_dimensao("Matriz")
    ma = cria_mat(m, n)
    ler_matriz("Matriz", ma)
    mt = retorna_transposta(ma)
    imprime_mat("Matriz Transposta ", mt)
    imprime_mat("Matriz Transposta Numpy ", np.transpose(ma))


# vem a main da "aplicação"
# menu
opcao = 1
while opcao != 0:
    print("Menu de opcoes:")
    print("  0 - sair")
    print("  1 - multiplicar matrizes")
    print("  2 - multiplicar matriz por escalar")
    print("  3 - Maior, menor e soma dos elementos da matriz")
    print("  4 - determinante matriz 3x3 (Regra de Sarrus)")
    print("  5 - determinante matriz 4x4 (Teorema de Laplace)")
    print("  6 - transposta de matriz")
    opcao = int(input("  Qual sua opcao: "))
    if opcao == 0:
        break
    elif opcao == 1:
        multiplicacao_matrizes()
        # CHAMAR O EQUIVALENTE DO NUMPY E MOSTRAR OS RESULTADOS PARA COMPARAR
    elif opcao == 2:
        multiplicar_matriz_por_escalar()
    elif opcao == 3:
        maior_menor_soma()
    elif opcao == 4:
        det_Sarrus()
    elif opcao == 5:
        det_Laplace()
    elif opcao == 6:
        transposta()