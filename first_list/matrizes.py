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
        imprime_mat("Matriz A", ma)
        imprime_mat("Matriz B", mb)
        imprime_mat("Matriz R = A * B", mres)
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
        print ("Escolheu tres")
    elif opcao == 5:
        print ("Escolheu tres")
    elif opcao == 6:
        print ("Escolheu tres")